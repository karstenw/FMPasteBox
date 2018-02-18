#
#  FMPasteBoxAppDelegate.py
#  FMPasteBox
#

import sys
import os

import pprint
pp = pprint.pprint

import pdb
kwlog = True

import objc

import Foundation
NSObject = Foundation.NSObject
NSMutableDictionary = Foundation.NSMutableDictionary
NSData = Foundation.NSData

import AppKit
NSWindowController = AppKit.NSWindowController
NSApplication = AppKit.NSApplication
NSUserDefaults = AppKit.NSUserDefaults
NSMutableAttributedString = AppKit.NSMutableAttributedString
NSBeep = AppKit.NSBeep
NSPasteboard = AppKit.NSPasteboard

import FMPasteBoxTools
read_pb = FMPasteBoxTools.read_pb
makeunicode = FMPasteBoxTools.makeunicode
fmpPasteboardTypes = FMPasteBoxTools.fmpPasteboardTypes
additionalFMPPasteboardTypes = FMPasteBoxTools.additionalFMPPasteboardTypes
displaynameTypes = FMPasteBoxTools.displaynameTypes
datetimestamp = FMPasteBoxTools.datetimestamp


import FMPasteBoxVersion

import FMPasteBoxPrefController
PrefController = FMPasteBoxPrefController.FMPasteBoxPreferenceController

class FMPasteBoxAppDelegate(NSObject):

    menClipboardtype = objc.IBOutlet()
    butGetClipboard = objc.IBOutlet()
    butPushClipboard = objc.IBOutlet()
    tfXMLEditor = objc.IBOutlet()
    appWindow = objc.IBOutlet()

    def initialize(self):
        if kwlog:
            print "FMPasteBoxAppDelegate.initialize()"
        userdefaults = NSMutableDictionary.dictionary()
        userdefaults.setObject_forKey_(u"", u'txtFileMakerAppPath')
        userdefaults.setObject_forKey_(u"", u'txtExportsPath')
        userdefaults.setObject_forKey_(False, u'cbDoExports')
        NSUserDefaults.standardUserDefaults().registerDefaults_(userdefaults)
        self.preferenceController = None


    def awakeFromNib(self):
        # for later
        defaults = NSUserDefaults.standardUserDefaults()

        # set up type menu
        self.menClipboardtype.removeAllItems()
        menuItems = [ u"" ]
        menuItems.extend( displaynameTypes.keys() )
        menuItems.sort()
        for menuItem in menuItems:
            self.menClipboardtype.addItemWithTitle_( menuItem )
        self.menClipboardtype.setTitle_( u"" )
        # set up text view
        self.tfXMLEditor.setUsesFindPanel_(True)
        window = self.tfXMLEditor.window()
        window.makeFirstResponder_(self.tfXMLEditor)


    def applicationDidFinishLaunching_(self, notification):
        app = NSApplication.sharedApplication()
        app.activateIgnoringOtherApps_(True)
        window = self.tfXMLEditor.window()
        window.makeFirstResponder_(self.tfXMLEditor)


    @objc.IBAction
    def getClipboard_(self, sender):
        pasteboardContents = read_pb()
        if not pasteboardContents:
            # abort - nothing on pasteboard
            NSBeep()
            # we must return implicit None! Crashing otherwise.
            return
        defaults = NSUserDefaults.standardUserDefaults()
        exportClipboards = defaults.boolForKey_( u'cbDoExports' )
        if exportClipboards:
            exportFolder = makeunicode(defaults.objectForKey_( u'txtExportsPath' ))
            if os.path.exists( exportFolder ):
                d,t = FMPasteBoxTools.datetimestamp()
                dayFolder = os.path.join( exportFolder, d )
                sessionFolder = os.path.join( dayFolder, t)
                try:
                    exportItems = pasteboardContents.additionals[:]
                    exportItems.append( pasteboardContents )
                    for item in exportItems:
                        if not os.path.exists( sessionFolder ):
                            os.makedirs( sessionFolder )
                        name = item.typ.name
                        ext = item.typ.fileExt
                        data = item.data
                        path = os.path.join( sessionFolder, name + ext )
                        if ext == ".xml":
                            data = makeunicode( data )
                            data = data.encode( "utf-8" )
                        f = open(path, 'w')
                        f.write( data )
                        f.close()
                except Exception, err:
                    print
                    print "ADDITIONALS FAILED"
                    print err
                    print
        pbType = pasteboardContents.typ
        pbTypeName = pbType.name
        self.menClipboardtype.setTitle_( pbTypeName )
        self.tfXMLEditor.setString_( makeunicode( pasteboardContents.data ) )
        window = self.tfXMLEditor.window()
        window.makeFirstResponder_(self.tfXMLEditor)


    def textView(self):
        # model
        return makeunicode( self.tfXMLEditor.string() )


    @objc.IBAction
    def pushClipboard_(self, sender):
        # get text view data
        data = makeunicode(self.textView())
        data = data.encode("utf-8")
        l = len(data)
        nsdata = NSData.dataWithBytes_length_(data, l)
        
        # get pasteboard type
        pasteboardType = displaynameTypes.get( self.menClipboardtype.title(), u"" )
        if not pasteboardType:
            NSBeep()
            # we must return implicit None! Crashing otherwise.
            return
        # write to pasteboard
        pasteboard = NSPasteboard.generalPasteboard()
        pasteboard.clearContents()
        pasteboardTypeName = pasteboardType.pbname
        pasteboard.setData_forType_( nsdata, pasteboardTypeName)


    @objc.IBAction
    def showPreferencePanel_(self, sender):
        if self.preferenceController == None:
            self.preferenceController = PrefController.alloc().init()
        self.preferenceController.showWindow_( self.preferenceController )

