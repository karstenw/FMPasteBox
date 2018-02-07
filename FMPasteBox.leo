<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="karstenw.20180207130038.1" a="E"><vh>@clean FMPasteBox.py</vh>
<v t="karstenw.20180207130303.1"><vh>Declarations</vh></v>
</v>
<v t="karstenw.20180207130137.1" a="E"><vh>@clean FMPasteBoxAppDelegate.py</vh>
<v t="karstenw.20180207130300.1"><vh>Declarations</vh></v>
<v t="karstenw.20180207130300.2"><vh>class FMPasteBoxAppDelegate</vh>
<v t="karstenw.20180207130300.3"><vh>initialize</vh></v>
<v t="karstenw.20180207130300.4"><vh>getClipboard_</vh></v>
<v t="karstenw.20180207130300.5"><vh>pushClipboard_</vh></v>
<v t="karstenw.20180207130300.6"><vh>applicationDidFinishLaunching_</vh></v>
<v t="karstenw.20180207130300.7"><vh>showPreferencePanel_</vh></v>
</v>
</v>
<v t="karstenw.20180207130144.1" a="E"><vh>@clean FMPasteBoxPrefController.py</vh>
<v t="karstenw.20180207130257.1"><vh>Declarations</vh></v>
<v t="karstenw.20180207130257.2"><vh>class FMPasteBoxPreferenceController</vh>
<v t="karstenw.20180207130257.3"><vh>init</vh></v>
<v t="karstenw.20180207130257.4"><vh>windowWillClose_</vh></v>
<v t="karstenw.20180207130257.5"><vh>chooseFolder_</vh></v>
</v>
</v>
<v t="karstenw.20180207130148.1" a="E"><vh>@clean FMPasteBoxTools.py</vh>
<v t="karstenw.20180207130254.1"><vh>Declarations</vh></v>
<v t="karstenw.20180207130254.2"><vh>num2ostype</vh></v>
<v t="karstenw.20180207130254.3"><vh>ostype2num</vh></v>
<v t="karstenw.20180207130254.4"><vh>makeunicode</vh></v>
<v t="karstenw.20180207130254.5"><vh>cancelContinueAlert</vh></v>
<v t="karstenw.20180207130254.6"><vh>errorDialog</vh></v>
<v t="karstenw.20180207130254.7"><vh>getFileDialog</vh></v>
<v t="karstenw.20180207130254.8"><vh>getApplicationDialog</vh></v>
<v t="karstenw.20180207130254.9"><vh>getFolderDialog</vh></v>
<v t="karstenw.20180207130254.10"><vh>NSURL2str</vh></v>
<v t="karstenw.20180207130254.11"><vh>saveAsDialog</vh></v>
<v t="karstenw.20180207130254.12"><vh>getFileProperties</vh></v>
<v t="karstenw.20180207130254.13"><vh>setFileProperties</vh></v>
<v t="karstenw.20180207130254.14"><vh>datestring_nsdate</vh></v>
<v t="karstenw.20180207130254.15"><vh>setFileModificationDate</vh></v>
<v t="karstenw.20180207130254.16"><vh>uniquepath</vh></v>
<v t="karstenw.20180207130254.17"><vh>get_type_from_hexstring</vh></v>
<v t="karstenw.20180207130254.18"><vh>get_hexstring_for_type</vh></v>
<v t="karstenw.20180207130254.19"><vh>get_type_from_intstring</vh></v>
<v t="karstenw.20180207130254.20"><vh>get_flavor</vh></v>
<v t="karstenw.20180207130254.21"><vh>writePasteboardFlavour</vh></v>
<v t="karstenw.20180207130254.22"><vh>read_pb</vh></v>
<v t="karstenw.20180207130255.1"><vh>write_pb</vh></v>
<v t="karstenw.20180207130255.2"><vh>parseScriptForExport</vh></v>
</v>
<v t="karstenw.20180207130153.1" a="E"><vh>@clean FMPasteBoxVersion.py</vh>
<v t="karstenw.20180207130252.1"><vh>Declarations</vh></v>
</v>
<v t="karstenw.20180207130158.1" a="E"><vh>@clean fmpterms.py</vh>
<v t="karstenw.20180207130250.1"><vh>Declarations</vh></v>
</v>
<v t="karstenw.20180207130202.1" a="E"><vh>@clean setup.py</vh>
<v t="karstenw.20180207130247.1"><vh>Declarations</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="karstenw.20180207130038.1">@language python
@tabwidth -4
@others

</t>
<t tx="karstenw.20180207130137.1">@language python
@tabwidth -4
@others

</t>
<t tx="karstenw.20180207130144.1">@language python
@tabwidth -4
@others


</t>
<t tx="karstenw.20180207130148.1">@language python
@tabwidth -4
@others

</t>
<t tx="karstenw.20180207130153.1">@language python
@tabwidth -4
@others

</t>
<t tx="karstenw.20180207130158.1">@language python
@tabwidth -4
@others
</t>
<t tx="karstenw.20180207130202.1">@language python
@tabwidth -4
@others
</t>
<t tx="karstenw.20180207130247.1">"""
Script for building FMPasteBox

Usage:
    python setup.py py2app
"""
from distutils.core import setup
from setuptools.extension import Extension

import py2app

import FMPasteBoxVersion

setup(
    name = FMPasteBoxVersion.appname,
    version = FMPasteBoxVersion.version,
    description = FMPasteBoxVersion.description,
    long_description = FMPasteBoxVersion.longdescription,
    author = FMPasteBoxVersion.author,
    app=[{
        'script': "FMPasteBox.py",

        "plist": {
            "NSPrincipalClass": 'NSApplication',
            "CFBundleIdentifier": FMPasteBoxVersion.bundleID,
            "CFBundleName": FMPasteBoxVersion.appnameshort,
            "CFBundleSignature": FMPasteBoxVersion.creator,
            "CFBundleShortVersionString": FMPasteBoxVersion.version,
            "CFBundleGetInfoString": FMPasteBoxVersion.description,
            "NSHumanReadableCopyright": FMPasteBoxVersion.copyright,
        }
    }],

    data_files=[
        "English.lproj/MainMenu.nib",
        "English.lproj/Preferences.nib",
        #"English.lproj/FMPasteBoxDocument.nib",
        "+icon/FMPasteBox.icns",
        #"+icon/FMPasteBoxFile.icns",
        ],

    options={
        "py2app": {
            "iconfile": "+icon/FMPasteBox.icns",
            # "packages": [],
            "excludes": ["TkInter", 'Tcl', 'Tk'],
        }
    } )

</t>
<t tx="karstenw.20180207130250.1">version = 1.1
path = u'/Applications/FileMaker/FileMaker Pro 11 Advanced/FileMaker Pro Advanced.app'

classes = \
[('application', 'capp'),
 ('window', 'cwin'),
 ('document', 'docu'),
 ('database', 'cDB '),
 ('table', 'cTBL'),
 ('FileMaker_script', 'cSCP'),
 ('layout', 'ctbl'),
 ('field', 'ccol'),
 ('record', 'crow'),
 ('cell', 'ccel'),
 ('repetition', 'cREP'),
 ('request', 'cRQT'),
 ('menu_item', 'cmen'),
 ('menu', 'cmnu')]

enums = \
[('table', 'TABL'),
 ('view', 'VIEW'),
 ('read_only', 'nmod'),
 ('formulas_protected', 'fpro'),
 ('read_write', 'modf'),
 ('no_access', '\x00\x00\x00\x00'),
 ('read', '\x00\x00\x00\x01'),
 ('write', '\x00\x00\x00\x02'),
 ('update', '\x00\x00\x00\x04'),
 ('create', '\x00\x00\x00\x08'),
 ('delete', '\x00\x00\x00\x10'),
 ('read_write', '\x00\x00\x00\x03'),
 ('read_update', '\x00\x00\x00\x05'),
 ('read_create', '\x00\x00\x00\t'),
 ('read_delete', '\x00\x00\x00\x11'),
 ('write_update', '\x00\x00\x00\x06'),
 ('write_create', '\x00\x00\x00\n'),
 ('write_delete', '\x00\x00\x00\x12'),
 ('update_create', '\x00\x00\x00\x0c'),
 ('update_delete', '\x00\x00\x00\x14'),
 ('write_delete', '\x00\x00\x00\x18'),
 ('read_write_update', '\x00\x00\x00\x07'),
 ('read_write_create', '\x00\x00\x00\x0b'),
 ('read_write_delete', '\x00\x00\x00\x13'),
 ('write_update_create', '\x00\x00\x00\x0e'),
 ('write_update_delete', '\x00\x00\x00\x16'),
 ('update_create_delete', '\x00\x00\x00\x1c'),
 ('read_create_delete', '\x00\x00\x00\x19'),
 ('read_update_delete', '\x00\x00\x00\x15'),
 ('write_create_delete', '\x00\x00\x00\x1a'),
 ('read_update_create', '\x00\x00\x00\r'),
 ('no_delete', '\x00\x00\x00\x0f'),
 ('no_create', '\x00\x00\x00\x17'),
 ('no_update', '\x00\x00\x00\x1b'),
 ('no_read', '\x00\x00\x00\x1e'),
 ('no_write', '\x00\x00\x00\x1d'),
 ('full', '\x00\x00\x00\x1f'),
 ('ascending', '\x00\x00\x00\x00'),
 ('descending', '\x00\x00\x00\x01'),
 ('custom', '\x00\x00\x00\x04'),
 ('sum', 'TOTL'),
 ('count', 'CONT'),
 ('mean', 'MEAN'),
 ('standard_deviation', 'STDV'),
 ('average', 'AVRG'),
 ('minimum', 'MIN '),
 ('maximum', 'MAX '),
 ('unlocked', 'NOLK'),
 ('shared_lock', 'SHLK'),
 ('exclusive_lock', 'EXLK'),
 ('false', 'fals'),
 ('sharing_hidden', 'mltH'),
 ('true', 'true'),
 ('single', 'rSgl'),
 ('repeated', 'rFxd'),
 ('guest', 'pGST'),
 ('before_', 'befo'),
 ('after_', 'afte'),
 ('beginning_', 'bgng'),
 ('end_', 'end '),
 ('replace', 'rplc'),
 ('index', 'indx'),
 ('named', 'name'),
 ('ID_', 'ID  ')]

properties = \
[('best_type', 'pbst'),
 ('class_', 'pcls'),
 ('default_type', 'deft'),
 ('frontmost', 'pisf'),
 ('name', 'pnam'),
 ('version', 'vers'),
 ('bounds', 'pbnd'),
 ('visible', 'pvis'),
 ('index', 'pidx'),
 ('floating', 'isfl'),
 ('zoomable', 'iszm'),
 ('zoomed', 'pzum'),
 ('modal', 'pmod'),
 ('resizable', 'prsz'),
 ('has_close_box', 'hclb'),
 ('has_title_bar', 'ptit'),
 ('current_layout', 'pCLY'),
 ('current_record', 'pCRW'),
 ('current_table', 'pCTB'),
 ('current_cell', 'pCCL'),
 ('modified', 'imod'),
 ('multiuser', 'pMUr'),
 ('lock', 'pLCK'),
 ('access', 'pACS'),
 ('ID_', 'ID  '),
 ('protection', 'ppro'),
 ('kind', 'pKND'),
 ('choices', 'pCHS'),
 ('formula', 'pfor'),
 ('nulls_OK', 'pNLS'),
 ('repeats', 'pRPT'),
 ('repeat_size', 'pRPS'),
 ('unique_value', 'pUNQ'),
 ('globalValue', 'pGLL'),
 ('cellValue', 'vlue'),
 ('omitted', 'pOMT'),
 ('enabled', 'enbl'),
 ('item_number', 'itmn'),
 ('checked', 'pCHK')]

elements = \
[('applications', 'capp'),
 ('windows', 'cwin'),
 ('documents', 'docu'),
 ('databases', 'cDB '),
 ('tables', 'cTBL'),
 ('FileMaker_scripts', 'cSCP'),
 ('layouts', 'ctbl'),
 ('fields', 'ccol'),
 ('records', 'crow'),
 ('cells', 'ccel'),
 ('repetitions', 'cREP'),
 ('requests', 'cRQT'),
 ('menu_items', 'cmen'),
 ('menus', 'cmnu')]

commands = \
[('getURL', 'GURLGURL', [('for_accounts', 'pACT')]),
 ('exists', 'coredoex', []),
 ('show', 'miscmvis', []),
 ('close', 'coreclos', []),
 ('redo', 'miscredo', []),
 ('find', 'FMPRFIND', []),
 ('quit', 'aevtquit', []),
 ('cut', 'misccut ', []),
 ('get_remote_URL', 'FMPROPRM', []),
 ('open', 'aevtodoc', [('with_passwords', 'pPAS'), ('for_Accounts', 'pACT')]),
 ('create',
  'corecrel',
  [('new', 'kocl'),
   ('at', 'insh'),
   ('with_data', 'data'),
   ('with_properties', 'prdt')]),
 ('get_data', 'coregetd', [('as_', 'rtyp')]),
 ('event_info', 'coregtei', [('in_', 'wrcd')]),
 ('print_',
  'aevtpdoc',
  [('with_password', 'pPAS'),
   ('for_Accounts', 'pACT'),
   ('from_page', 'StPg'),
   ('to_page', 'NdPg'),
   ('with_copies', 'Cpis')]),
 ('duplicate', 'coreclon', [('to', 'insh')]),
 ('save', 'coresave', []),
 ('data_size', 'coredsiz', [('as_', 'rtyp')]),
 ('go_to', 'FMPRGOTO', []),
 ('sort', 'DATASORT', [('by', 'SRTE'), ('in_order', 'SRTT')]),
 ('undo', 'miscundo', []),
 ('set_data', 'coresetd', [('to', 'data')]),
 ('copy', 'misccopy', []),
 ('paste', 'miscpast', []),
 ('count', 'corecnte', [('class_', 'kocl')]),
 ('do_script', 'miscdosc', []),
 ('class_info', 'coreqobj', [('in_', 'wrcd')]),
 ('do_menu', 'miscmenu', [('menu_named', 'menn')]),
 ('delete', 'coredelo', [])]
</t>
<t tx="karstenw.20180207130252.1">import os

appname ="FMPasteBox"
appnameshort = "FMPasteBox"
author = "Karsten Wolf"

years = "2018"
copyright = 'Copyright %s %s' % (years, author)

version = "0.1.0"
creator = 'KWFP'
bundleID = "org.kw.FMPasteBox"

description = (u"Filemaker Pasteboard interface and editor")
longdescription = u"""FMPasteBox is a Mac OS X application..."""

# 
#user_agent = "%s/%s +https://github.com/karstenw/FMPasteBox" % (appname, version)

#document_creator = "Created by %s %s" % (appname, version)

#cachefolder = os.path.expanduser("~/Library/Application Support/%s" % appname )

developmentversion = False
</t>
<t tx="karstenw.20180207130254.1"># -*- coding: utf-8 -*-

"""Some tools which are needed by most files.
"""

import sys
import os
import re
import struct
import traceback
import datetime
import unicodedata

import xml.etree.cElementTree
ElementTree = xml.etree.cElementTree

import mactypes
import appscript
asc = appscript

import FMPasteBoxVersion
kwdbg = FMPasteBoxVersion.developmentversion
kwlog = FMPasteBoxVersion.developmentversion

import pdb

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

# seems like the standart naming scheme for the pasteboard server
re_pbtype = re.compile( u"CorePasteboardFlavorType 0x([A-F0-9]{,8})")

g_pboard = NSPasteboard.generalPasteboard()


#
# tools
#

</t>
<t tx="karstenw.20180207130254.10">def NSURL2str( nsurl ):
    if isinstance(nsurl, NSURL):
        return str(nsurl.absoluteString())
    return nsurl

#
# File save dialog
#
# SHOULD NOT BE USED ANYMORE (NSDocument handling)
</t>
<t tx="karstenw.20180207130254.11">def saveAsDialog(path):
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


</t>
<t tx="karstenw.20180207130254.12">def getFileProperties( theFile ):
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


</t>
<t tx="karstenw.20180207130254.13">def setFileProperties( theFile, props ):
    sfm = NSFileManager.defaultManager()
    return sfm.changeFileAttributes_atPath_( props, theFile )


</t>
<t tx="karstenw.20180207130254.14">def datestring_nsdate( dt=datetime.datetime.now() ):
    now = str(dt)
    now = now[:19]
    now = now + " +0000"
    return now


</t>
<t tx="karstenw.20180207130254.15">def setFileModificationDate( filepath, modfdt ):
    l = getFileProperties( filepath )
    date = Foundation.NSDate.dateWithString_( datestring_nsdate( modfdt ) )
    l['NSFileModificationDate'] = date
    setFileProperties( filepath, l)
    folder, filename = os.path.split( filepath )
    print "Setting file(%s) modification date to %s" % (filename, repr(modfdt))


</t>
<t tx="karstenw.20180207130254.16">def uniquepath(folder, filenamebase, ext, nfill=3, startindex=1, sep="_", always=True):
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

        if n &gt;= 10**nfill:
            nfill = nfill + 1

        if not os.path.exists(fullpath):
            return fullpath

        n += 1

#
# pasteboard utilities
#

</t>
<t tx="karstenw.20180207130254.17">def get_type_from_hexstring( hexstring ):
    """Extract the 4-char macroman type code from the pasteboard type name.
    
    
    """
    h = int(hexstring, 16)
    s = struct.pack("&gt;I", h)
    s = unicode(s, 'macroman')
    return s


</t>
<t tx="karstenw.20180207130254.18">def get_hexstring_for_type( typ_ ):
    """
    """
    s = struct.pack( "BBBB", typ_ )
    i = struct.unpack( "&gt;I", s)
    return hex(i)

</t>
<t tx="karstenw.20180207130254.19">def get_type_from_intstring( intstring ):
    h = int(intstring)
    s = struct.pack("&gt;I", h)
    s = unicode(s, 'macroman')
    return s


</t>
<t tx="karstenw.20180207130254.2">def num2ostype( num ):
    if num == 0:
        return '????'
    s = struct.pack("&gt;I", num)
    return makeunicode(s, "macroman")


</t>
<t tx="karstenw.20180207130254.20">def get_flavor(s):
    """Return the 4-char type from a pasteboard name
    """

    m = re_pbtype.match(s)
    u = ""
    if m:
        t = m.groups()[0]
        u = get_type_from_hexstring(t)
    return u


</t>
<t tx="karstenw.20180207130254.21">def writePasteboardFlavour( folder, basename, ext, data ):
    p = uniquepath(folder, basename, ext)
    if data:
        f = open ( p, 'wb')
        f.write( data )
        f.close()




</t>
<t tx="karstenw.20180207130254.22">def read_pb( desiredTypes=None, writeFiles=True ):

    result = {}
    
    pbtypes = g_pboard.types()
    fname = "fmp_clip"
    for t in pbtypes:

        if desiredTypes:
            if not t in desiredTypes:
                continue

        try:
            mactype = ""
            data = g_pboard.dataForType_( t )
            
            if not data:
                continue

            data = str( data )
    
            t = t.encode("utf-8")
    
            print
            print t, 
            if t.startswith( 'CorePasteboardFlavorType' ):
                mactype = get_flavor(t)
            print mactype

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
            
            # FMPA 11
            # XMFN - 0x584D464E - Custom Functions
            
            basename = t
            ext = ".xml"
            # if one of the FMP types, add an xml extension to the output file
            if mactype in ( 'XMFD', 'XMTB', 'XMSC', 'XMSS', 'XMLO', 'XMFN'):
                if writeFiles:
                    writePasteboardFlavour( "./", basename, ".xml", data )
                result[basename+'.xml'] = data
            # handle pdf
            elif t == u'Apple PDF pasteboard type':
                if writeFiles:
                    writePasteboardFlavour( "./", basename, ".pdf", data )
                result[basename+'.pdf'] = data

            # handle PICT
            elif t == u'Apple PICT pasteboard type':
                # pdb.set_trace()
                s = chr(0) * 512
                if not data.startswith( s ):
                    data = s + data
                if writeFiles:
                    writePasteboardFlavour( "./", basename, ".pict", data )
                result[basename+'.pict'] = data

            # generic
            else:
                if writeFiles:
                    writePasteboardFlavour( "./", t + "_" + mactype, ".data", data )
                result[t+ '_' + mactype + '.data'] = data

        except Exception, v:
            print v
            pdb.set_trace()
            pp(locals())
            print
    return result

</t>
<t tx="karstenw.20180207130254.3">def ostype2num( ostype ):
    return struct.pack('BBBB', list(ostype))


</t>
<t tx="karstenw.20180207130254.4">def makeunicode(s, srcencoding="utf-8", normalizer="NFC"):
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
</t>
<t tx="karstenw.20180207130254.5">def cancelContinueAlert(title, message, butt1="OK", butt2=False):
    """Run a generic Alert with buttons "Weiter" &amp; "Abbrechen".

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


</t>
<t tx="karstenw.20180207130254.6">def errorDialog( message="Error", title="Some error occured..."):
    return cancelContinueAlert(title, message)


#
# Open File
#
</t>
<t tx="karstenw.20180207130254.7">def getFileDialog(multiple=False):
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(multiple)
    rval = panel.runModalForTypes_( None )
    if rval:
        return [t for t in panel.filenames()]
    return []


</t>
<t tx="karstenw.20180207130254.8">def getApplicationDialog():
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    rval = panel.runModalForTypes_( ['app'] )
    if rval:
        l = [makeunicode(t.path()) for t in panel.URLs()]
        return l[0]
    return ""


</t>
<t tx="karstenw.20180207130254.9">def getFolderDialog(multiple=False):
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(False)
    panel.setCanChooseDirectories_(True)
    panel.setAllowsMultipleSelection_(multiple)
    rval = panel.runModalForTypes_([])
    if rval:
        return [t for t in panel.filenames()]
    return []


</t>
<t tx="karstenw.20180207130255.1">def write_pb(typ_, data):
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
</t>
<t tx="karstenw.20180207130255.2">def parseScriptForExport( argumentfiles ):

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

</t>
<t tx="karstenw.20180207130257.1">#
#   FMPasteBoxPreferenceController.py
#
#   Created by Karsten Wolf on 07.02.18.
#   Copyright 2018 Karsten Wolf. All rights reserved.
#

import objc

import Foundation
NSUserDefaults = Foundation.NSUserDefaults


import AppKit
NSApplication = AppKit.NSApplication
NSWindowController = AppKit.NSWindowController

import FMPasteBoxTools



</t>
<t tx="karstenw.20180207130257.2">class FMPasteBoxPreferenceController (NSWindowController):

    butSetFileMakerAppPath = objc.IBOutlet()

    txtFileMakerAppPath = objc.IBOutlet()

    @others
</t>
<t tx="karstenw.20180207130257.3">def init(self):
    self = self.initWithWindowNibName_("Preferences")

    wnd = self.window()
    wnd.setTitle_( u"FMPasteBox Preferences" )
    wnd.setDelegate_( self )

    defaults = NSUserDefaults.standardUserDefaults()
    self.txtFileMakerAppPath.setStringValue_( defaults.objectForKey_( u'txtFileMakerAppPath') )
    return self


</t>
<t tx="karstenw.20180207130257.4">def windowWillClose_(self, notification):
    defaults = NSUserDefaults.standardUserDefaults()
    defaults.setObject_forKey_(self.txtFileMakerAppPath.stringValue(),   u'txtFileMakerAppPath')



</t>
<t tx="karstenw.20180207130257.5">@objc.IBAction
def chooseFolder_(self, sender):
    if sender == self.butSetFileMakerAppPath:
        folders = FMPasteBoxTools.getApplicationDialog()
        if folders:
            self.txtFileMakerAppPath.setStringValue_( folders )

</t>
<t tx="karstenw.20180207130300.1">#
#  FMPasteBoxAppDelegate.py
#  FMPasteBox
#

import pdb
kwlog = True

import objc

import Foundation
NSObject = Foundation.NSObject
NSMutableDictionary = Foundation.NSMutableDictionary

import AppKit
NSWindowController = AppKit.NSWindowController
NSApplication = AppKit.NSApplication
NSUserDefaults = AppKit.NSUserDefaults

import FMPasteBoxTools
import FMPasteBoxVersion

import FMPasteBoxPrefController
PrefController = FMPasteBoxPrefController.FMPasteBoxPreferenceController

</t>
<t tx="karstenw.20180207130300.2">class FMPasteBoxAppDelegate(NSObject):
    menClipboardtype = objc.IBOutlet()

    butGetClipboard = objc.IBOutlet()

    butPushClipboard = objc.IBOutlet()

    @others
</t>
<t tx="karstenw.20180207130300.3">def initialize(self):
    if kwlog:
        print "FMPasteBoxAppDelegate.initialize()"
    userdefaults = NSMutableDictionary.dictionary()
    userdefaults.setObject_forKey_(u"", u'txtFileMakerAppPath')
    NSUserDefaults.standardUserDefaults().registerDefaults_(userdefaults)
    self.preferenceController = None

</t>
<t tx="karstenw.20180207130300.4">@objc.IBAction
def getClipboard_(self, sender):
    print "getClipboard_"
    # old schema
    read_pb()

</t>
<t tx="karstenw.20180207130300.5">@objc.IBAction
def pushClipboard_(self, sender):
    print "pushClipboard_"
    # old schema
    fnroot, fnext = os.path.splitext( fn )
    theType = makeunicode(fnroot)
    fob = open(theFile, "r")
    s = fob.read()
    fob.close()
    s = makeunicode( s )
    write_pb(theType, s)


</t>
<t tx="karstenw.20180207130300.6">def applicationDidFinishLaunching_(self, notification):
    app = NSApplication.sharedApplication()
    app.activateIgnoringOtherApps_(True)

    # ugly hack
    wins = app.windows()
    if not wins:
        return
    win = wins[0]
    controller = win.windowController()


</t>
<t tx="karstenw.20180207130300.7">@objc.IBAction
def showPreferencePanel_(self, sender):
    if self.preferenceController == None:
        self.preferenceController = PrefController.alloc().init()
    self.preferenceController.showWindow_( self.preferenceController )


</t>
<t tx="karstenw.20180207130303.1">#
#  FMPasteBox.py
#  FMPasteBox
#

import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

import FMPasteBoxAppDelegate


if __name__ == '__main__':
    AppHelper.runEventLoop()
</t>
</tnodes>
</leo_file>
