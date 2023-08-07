# -*- coding: utf-8 -*-

from __future__ import print_function

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

import xml.etree.ElementTree
ElementTree = xml.etree.ElementTree

import mactypes
import appscript
asc = appscript

import pdb
import FMPasteBoxVersion
kwdbg = FMPasteBoxVersion.developmentversion
kwlog = FMPasteBoxVersion.developmentversion

import pprint
pp = pprint.pprint

import urllib

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


# py3 stuff

py3 = False
try:
    unicode('')
    punicode = unicode
    pstr = str
    punichr = unichr
except NameError:
    punicode = str
    pstr = bytes
    py3 = True
    punichr = chr

def num2ostype( num ):
    if num == 0:
        return '????'
    s = struct.pack(">I", num)
    return makeunicode(s, "macroman")


def ostype2num( ostype ):
    return struct.pack('BBBB', list(ostype))


def makeunicode(s, srcencoding="utf-8", normalizer="NFC"):
    if type(s) not in (punicode, pstr):
        s = str( s )
    if type(s) != punicode:
        s = punicode(s, srcencoding)
    s = unicodedata.normalize(normalizer, s)
    return s


def NSURL2str( nsurl ):
    if isinstance(nsurl, NSURL):
        return str(nsurl.absoluteString())
    return nsurl


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
    print( "Setting file(%s) modification date to %s" % (filename, repr(modfdt )))


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


def gethashval( s ):
    m = hashlib.sha1()
    size = len(s)

    t = b"blob %i\0%s" % (size, s)
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


def datetimestamp( dt=None ):
    # '2018-02-17 19:41:02'
    if not dt:
        dt = datetime.datetime.now()
    now = str(dt)
    now = now[:19]
    d, t = now.split()
    t = t.replace(':', '')
    return (d,t)


def get_type_from_hexstring( hexstring ):
    """Extract the 4-char macroman type code from the pasteboard type name."""
    h = int(hexstring, 16)
    s = struct.pack(">I", h)
    s = makeunicode(s, 'macroman')
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
    s = makeunicode(s, 'macroman')
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

# fmpa 18
# XMVL - 0x584D564C - Value Lists
# public.utf16-plain-text - Custom Menu Set Catalogue
# public.utf16-plain-text - Custom Menu Catalogue


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

# FMPA 18
# XMVL
# Custom menu set - XML text



# FileMaker Developer Pasteboard types
# beides binaerformate
# FTR5 - 0x46545235 - 
# FMP5


class PasteboardType(object):
    canonicalTypes = {
        u'com.adobe.pdf': u'Apple PDF pasteboard type',
        u'public.jpeg': u"CorePasteboardFlavorType 0x4A504547",
        u'NeXT TIFF v4.0 pasteboard type': u'public.tiff',
        # XML2
        u'dyn.ah62d4rv4gk8zuxnqgk': u"CorePasteboardFlavorType 0x584D4C32",
        
    }

    def __init__(self, pbname, typ, dataType, name, fileExt):
        self.pbname = pbname
        self.typ = typ
        self.dataType = dataType
        self.name = name
        self.fileExt = fileExt
        self.canonicalType = self.canonicalTypes.get( pbname, pbname )


    def __repr__(self):
        return u"PasteboardType(%s, %s, %s, %s, %s, %s)" % (
                repr(self.pbname),
                repr(self.typ),
                repr(self.dataType),
                repr(self.name),
                repr(self.fileExt),
                repr(self.canonicalType),)


class PasteboardEntry(object):
    def __init__(self, name, data, typ):
        self.name = name
        self.data = data
        self.typ = typ
        self.additionals = []


    def __repr__(self):
        return u"PasteboardEntry(%s, data[%i], %s, %s)" % (
                repr(self.name),
                len(self.data),
                repr(self.typ),
                repr(self.additionals))


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
# "Custom Functions" -> PasteboardType(u"CorePasteboardFlavorType 0x584D464E",...
for typeName in fmpPasteboardTypes:
    typ = fmpPasteboardTypes[typeName]
    displaynameTypes[typ.name] = typ


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
                        "Layout Objects PICT Image (obsolete)", '.pict'),

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

    additionals = []
    pasteboard = NSPasteboard.generalPasteboard()
    pbTypeNames = pasteboard.types()

    
    # additionalFMPPasteboardTypes

    for pbTypeName in pbTypeNames:
        if 1:
            print( "pbTypeName:", pbTypeName )

        pbType = mainType = None

        if pbTypeName in fmpPasteboardTypes:
            pbType = fmpPasteboardTypes.get( pbTypeName )
            mainType = True
        elif pbTypeName in additionalFMPPasteboardTypes:
            pbType = additionalFMPPasteboardTypes.get( pbTypeName )
            mainType = False

        if pbType == None:
            continue

        try:

            # pdb.set_trace()

            s = pasteboard.dataForType_( pbTypeName )
            data = s.bytes().tobytes()

            # dont load duplicate data
            hashval, _ = gethashval( data )
            if hashval in hashes:
                continue
            hashes.add( hashval )
            
            if mainType:
                data = makeunicode(data)

            pbTypeName = pbType.canonicalType
            
            pbEntry = PasteboardEntry(pbTypeName, data, pbType)
            
            if mainType:
                result = pbEntry
            else:
                additionals.append( pbEntry )

        except Exception as v:
            print( v )
            # pdb.set_trace()
            pp(locals())
            print()

    if result:
        result.additionals = additionals

    if 1:
        print()
        print( "result = " )
        pp(result)
        print()
    return result

