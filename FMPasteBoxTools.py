# -*- coding: utf-8 -*-

"""Some tools which are needed by most files.
"""

import sys
import os
import re
import struct
import traceback
import datetime
import unicodedata
import hashlib

import xml.etree.cElementTree
ElementTree = xml.etree.cElementTree

import mactypes
import appscript
asc = appscript

import FMPasteBoxVersion
kwdbg = FMPasteBoxVersion.developmentversion
kwlog = FMPasteBoxVersion.developmentversion

import pprint
pp = pprint.pprint

import pdb
kwdbg = True
kwlog = True

import urllib
import urlparse

import objc

import Foundation
NSURL = Foundation.NSURL
NSFileManager = Foundation.NSFileManager
NSUserDefaults = Foundation.NSUserDefaults
NSString = Foundation.NSString

import AppKit
NSOpenPanel = AppKit.NSOpenPanel
NSAlert = AppKit.NSAlert
NSSavePanel = AppKit.NSSavePanel
NSFileHandlingPanelOKButton  = AppKit.NSFileHandlingPanelOKButton
NSPasteboard = AppKit.NSPasteboard
NSPasteboardCommunicationException = AppKit.NSPasteboardCommunicationException


#
# globals
#


#
# tools
#

def num2ostype( num ):
    if num == 0:
        return '????'
    s = struct.pack(">I", num)
    return makeunicode(s, "macroman")


def ostype2num( ostype ):
    return struct.pack('BBBB', list(ostype))


def makeunicode(s, srcencoding="utf-8", normalizer="NFC"):
    try:
        if type(s) not in (unicode, objc.pyobjc_unicode):
            s = unicode(s, srcencoding)
    except TypeError:
        print "makeunicode type conversion error"
        print "FAILED converting", type(s), "to unicode"
    s = unicodedata.normalize(normalizer, s)
    return s




#
# dialogs
#
def NSURL2str( nsurl ):
    if isinstance(nsurl, NSURL):
        return str(nsurl.absoluteString())
    return nsurl

#
# File save dialog
#
# SHOULD NOT BE USED ANYMORE (NSDocument handling)
def getFileProperties( theFile ):
    """
    """
    sfm = NSFileManager.defaultManager()
    props = sfm.fileAttributesAtPath_traverseLink_( theFile, True )
    if not props:
        return {}
    mtprops = props.mutableCopy()
    mtprops.removeObjectsForKeys_( [
        u"NSFileExtensionHidden",
        u"NSFileGroupOwnerAccountID",
        u"NSFileGroupOwnerAccountName",
        u"NSFileOwnerAccountID",
        u"NSFileOwnerAccountName",
        #u"NSFilePosixPermissions",
        #u"NSFileReferenceCount",
        # u"NSFileSize",
        #u"NSFileSystemFileNumber",
        u"NSFileSystemNumber",
        u"NSFileType",
        # u"NSFileHFSCreatorCode",
        # u"NSFileHFSTypeCode",
        #u"NSFileCreationDate"
        ] )
    return mtprops


def setFileProperties( theFile, props ):
    sfm = NSFileManager.defaultManager()
    return sfm.changeFileAttributes_atPath_( props, theFile )


def datestring_nsdate( dt=datetime.datetime.now() ):
    now = str(dt)
    now = now[:19]
    now = now + " +0000"
    return now


def setFileModificationDate( filepath, modfdt ):
    l = getFileProperties( filepath )
    date = Foundation.NSDate.dateWithString_( datestring_nsdate( modfdt ) )
    l['NSFileModificationDate'] = date
    setFileProperties( filepath, l)
    folder, filename = os.path.split( filepath )
    print "Setting file(%s) modification date to %s" % (filename, repr(modfdt))


def uniquepath(folder, filenamebase, ext, nfill=3, startindex=1, sep="_", always=True):
    """
    """
    folder = os.path.abspath( folder )
    
    if not always:
        path = os.path.join(folder, filename + ext )
        if not os.path.exists( path ):
            return path

    n = startindex
    while True:
        serialstring = str(n).rjust(nfill, "0")

        filename = filenamebase + sep + serialstring + ext

        fullpath = os.path.join(folder, filename)

        if n >= 10**nfill:
            nfill = nfill + 1

        if not os.path.exists(fullpath):
            return fullpath

        n += 1

#
# pasteboard utilities
#

def gethashval( s ):
    m = hashlib.sha1()
    size = len(s)

    t = "blob %i\0%s" % (size, s)
    m.update(t)
    return  (m.hexdigest(), size)


def cancelContinueAlert(title, message, butt1="OK", butt2=False):
    """Run a generic Alert with buttons "Weiter" & "Abbrechen".

       Returns True if "Weiter"; False otherwise
    """
    alert = NSAlert.alloc().init()
    alert.setAlertStyle_( 0 )
    alert.setInformativeText_( title )
    alert.setMessageText_( message )
    alert.setShowsHelp_( False )
    alert.addButtonWithTitle_( butt1 )

    if butt2:
        # button 2 has keyboard equivalent "Escape"
        button2 = alert.addButtonWithTitle_( butt2 )
        button2.setKeyEquivalent_( unichr(27) )

    f = alert.runModal()
    return f == AppKit.NSAlertFirstButtonReturn


def errorDialog( message="Error", title="Some error occured..."):
    return cancelContinueAlert(title, message)


#
# Open File
#
def getFileDialog(multiple=False):
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(multiple)
    rval = panel.runModalForTypes_( None )
    if rval:
        return [t for t in panel.filenames()]
    return []


def getApplicationDialog():
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    rval = panel.runModalForTypes_( ['app'] )
    if rval:
        l = [makeunicode(t.path()) for t in panel.URLs()]
        return l[0]
    return ""


def getFolderDialog(multiple=False):
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(False)
    panel.setCanChooseDirectories_(True)
    panel.setAllowsMultipleSelection_(multiple)
    rval = panel.runModalForTypes_([])
    if rval:
        return [t for t in panel.filenames()]
    return []


def saveAsDialog(path):
    panel = NSSavePanel.savePanel()

    if path:
        panel.setDirectory_( path )

    panel.setMessage_( u"Save as OPML" )
    panel.setExtensionHidden_( False )
    panel.setCanSelectHiddenExtension_(True)
    panel.setRequiredFileType_( u"opml" )
    if path:
        if not os.path.isdir( path ):
            folder, fle = os.path.split(path)
        else:
            folder = path
            fle = "Untitled.opml"
        rval = panel.runModalForDirectory_file_(folder, fle)
    else:
        rval = panel.runModal()

    if rval == NSFileHandlingPanelOKButton:
        return panel.filename()
    return False


def get_type_from_hexstring( hexstring ):
    """Extract the 4-char macroman type code from the pasteboard type name.
    
    
    """
    h = int(hexstring, 16)
    s = struct.pack(">I", h)
    s = unicode(s, 'macroman')
    return s


def get_hexstring_for_type( typ_ ):
    """
    """
    s = struct.pack( "BBBB", typ_ )
    i = struct.unpack( ">I", s)
    return hex(i)

def get_type_from_intstring( intstring ):
    h = int(intstring)
    s = struct.pack(">I", h)
    s = unicode(s, 'macroman')
    return s


def get_flavor(s):
    """Return the 4-char type from a pasteboard name
    """
    
    # seems like the standart naming scheme for the pasteboard server
    re_pbtype = re.compile( u"CorePasteboardFlavorType 0x([A-F0-9]{,8})")

    m = re_pbtype.match(s)
    result = ""
    if m:
        t = m.groups()[0]
        result = get_type_from_hexstring(t)
    return result


def writePasteboardFlavour( folder, basename, ext, data ):
    p = uniquepath(folder, basename, ext)
    if data:
        f = open ( p, 'wb')
        f.write( data )
        f.close()




# fmpa 15
# XML2 - 0x584D4C32 - generic xml for layout objects

# FMPA 11
# XMFN - 0x584D464E - Custom Functions

# FileMaker Advanced Pasteboard types    
# XMFD - 0x584D4644 - fields
# XMTB - 0x584D5442 - basetables
# XMSC - 0x584D5343 - scripts
# XMSS - 0x584D5353 - script step
# XMLO - 0x584D4C4F - layout objects


# FileMaker Developer Pasteboard types
# beides binaerformate
# FTR5 - 0x46545235 - 
# FMP5


class PasteboardType(object):
    def __init__(self, pbname, typ, dataType, name, fileExt):
        self.pbname = pbname
        self.typ = typ
        self.dataType = dataType
        self.name = name
        self.fileExt = fileExt
        self.alternates = []
    
    def __repr__(self):
        return u"PasteboardType(%s, %s, %s, %s, %s)" % (
                repr(self.pbname),
                repr(self.typ),
                repr(self.dataType),
                repr(self.name),
                repr(self.fileExt))
        

class PasteboardEntry(object):
    def __init__(self, name, data, typ):
        self.name = name
        self.data = data
        self.typ = typ

    def __repr__(self):
        return u"PasteboardEntry(%s, data[%i], %s)" % (
                repr(self.name),
                len(self.data),
                repr(self.typ))

fmpPasteboardTypes = {
    u"CorePasteboardFlavorType 0x584D4C32":
        PasteboardType(u"CorePasteboardFlavorType 0x584D4C32",
                        'XML2', 'fullXML', "Layout Objects", '.xml'),

    u"CorePasteboardFlavorType 0x584D5442":
        PasteboardType(u"CorePasteboardFlavorType 0x584D5442",
                        'XMTB', 'snippetXML', "Base Tables", '.xml'),


    u"CorePasteboardFlavorType 0x584D4644":
        PasteboardType(u"CorePasteboardFlavorType 0x584D4644",
                        'XMFD', 'snippetXML', "Fields", '.xml'),

    u"CorePasteboardFlavorType 0x584D5343":
        PasteboardType(u"CorePasteboardFlavorType 0x584D5343",
                        'XMSC', 'snippetXML', "Scripts", '.xml'),

    u"CorePasteboardFlavorType 0x584D5353":
        PasteboardType(u"CorePasteboardFlavorType 0x584D5353",
                        'XMSS', 'snippetXML', "Script Steps", '.xml'),

    u"CorePasteboardFlavorType 0x584D464E":
        PasteboardType(u"CorePasteboardFlavorType 0x584D464E",
                        'XMFN', 'snippetXML', "Custom Functions", '.xml'),

    u"CorePasteboardFlavorType 0x584D4C4F":
        PasteboardType(u"CorePasteboardFlavorType 0x584D4C4F",
                        'XMLO', 'snippetXML', "Layout Objects (obsolete)", '.xml'),
}


displaynameTypes = {}
for typeName in fmpPasteboardTypes:
    typ = fmpPasteboardTypes[typeName]
    displaynameTypes[typ.name] = typ

if kwlog:
    pp(displaynameTypes)

additionalFMPPasteboardTypes = {
    u"CorePasteboardFlavorType 0x4A504547":
        PasteboardType(u"CorePasteboardFlavorType 0x4A504547",
                        'JPEG', 'binaryData',
                        "Layout Objects JPEG Image", '.jpg'),

    u'Apple PDF pasteboard type':
        PasteboardType(u'Apple PDF pasteboard type',
                        'PDF', 'binaryData',
                        "Layout Objects PDF Image", '.pdf'),

    u'com.adobe.pdf':
        PasteboardType(u'com.adobe.pdf',
                        'PDF', 'binaryData',
                        "Layout Objects PDF Image", '.pdf'),

    u'Apple PICT pasteboard type':
        PasteboardType(u'Apple PICT pasteboard type',
                        'PICT', 'binaryData',
                        "Layout Objects PICT Image (obsolete)", '.pic'),

    u'NeXT TIFF v4.0 pasteboard type':
        PasteboardType(u'NeXT TIFF v4.0 pasteboard type',
                        'TIFF', 'binaryData',
                        "Layout Objects TIFF Image", '.tif'),

    u'public.jpeg':
        PasteboardType(u'public.jpeg',
                        'JPEG', 'binaryData',
                        "Layout Objects JPEG Image", '.jpg'),

    u'public.tiff':
        PasteboardType(u'public.tiff',
                        'TIFF', 'binaryData',
                        "Layout Objects TIFF Image", '.tif'),
}


def read_pb():
    result = None
    hashes = set()

    # pdb.set_trace()

    pasteboard = NSPasteboard.generalPasteboard()
    pbTypeNames = pasteboard.types()

    # additionalFMPPasteboardTypes

    for pbTypeName in pbTypeNames:

        pbType = None
        if pbTypeName in fmpPasteboardTypes:
            pbType = fmpPasteboardTypes.get( pbTypeName, pbTypeName )
            maintype = True
        else:
            continue
            # NOT NOW
            #if pbTypeName in additionalFMPPasteboardTypes:
            #    pbType = additionalFMPPasteboardTypes.get( pbTypeName )
            #    maintype = False


        if pbTypeName == None:
            continue

        try:
            s = pasteboard.dataForType_( pbTypeName )
            data = s.bytes().tobytes()

            # dont load duplicate data
            hashval, _ = gethashval( data )
            if hashval in hashes:
                continue
            hashes.add( hashval )
            
            data = makeunicode(data)

            result = PasteboardEntry(pbTypeName, data, pbType)
            return result

        except Exception, v:
            print v
            # pdb.set_trace()
            pp(locals())
            print

    # package it
    
    return result


def write_pb(typ_, data):
    # declare my type
    
    g_pboard.declareTypes_owner_([typ_], None)

    ok = "NOPE"
    try:
        # write it to clipboard
        ok = g_pboard.setString_forType_(data, typ_)
    except NSPasteboardCommunicationException, v:
        print "Copy failed"
        pp(v)
    pp(ok)


# elaborate
#
# this is hacky
#
def parseScriptForExport( argumentfiles ):

    pdb.set_trace()
    
    for af in argumentfiles:
        af = os.path.abspath( af )
        # folder of the ddr summary file
        xml_folder = os.path.dirname( af )

        # summary section
        xmltree = ElementTree.parse( af )
        root = xmltree.getroot()

        # get all files for this DDR
        scripts = root.findall( "Script" )

        # pdb.set_trace()

        i = 0
        for script in scripts:

            prefix = "00" + str(i)
            prefix = prefix[-2:]
            prefix = prefix + "_"
            curr_output_name = prefix + "default_out.tab"
            outfilepath = os.path.join( xml_folder, curr_output_name)
            outfile = open(outfilepath, 'w')

            name = script.attrib['name']

            for scriptstep in script.getiterator("Step"):

                stepname = scriptstep.attrib["name"]

                if stepname == "Set Variable":
                    for value in scriptstep:
                        for calculation in value:
                            v = calculation.text
                            if '/' in v:
                                v = v.strip("\r\n \t\"")
                                w = v.split('/')
                                curr_output_name = w[-1]
                                basename, ext = os.path.splitext(curr_output_name)
                                curr_output_name = basename + "_fieldnames" + ext
                                outfile.close()
                                outfilepath = os.path.join( xml_folder, curr_output_name)
                                outfile = open(outfilepath, 'w')
                                print
                                print "# '%s'" % curr_output_name.encode("utf-8")

                elif stepname == "Export Records":
                    for exportentries in scriptstep.getiterator("ExportEntries"):
                        for exportentry in exportentries.getiterator("ExportEntry"):
                            for field in exportentry.getiterator("Field"):
                                fieldname = field.attrib['name']
                                fieldname = fieldname.encode("utf-8")
                                fieldtable = field.attrib['table']
                                fieldtable = fieldtable.encode("utf-8")
                                print "'%s'\t'%s'" % (fieldname, fieldtable)
                                outfile.write( "%s\n" % (fieldname,) )
            outfile.close()


