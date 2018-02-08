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
write_pb = FMPasteBoxTools.write_pb
makeunicode = FMPasteBoxTools.makeunicode
fmpPasteboardTypes = FMPasteBoxTools.fmpPasteboardTypes
additionalFMPPasteboardTypes = FMPasteBoxTools.additionalFMPPasteboardTypes
displaynameTypes = FMPasteBoxTools.displaynameTypes

import FMPasteBoxVersion

import FMPasteBoxPrefController
PrefController = FMPasteBoxPrefController.FMPasteBoxPreferenceController

class FMPasteBoxAppDelegate(NSObject):

    menClipboardtype = objc.IBOutlet()
    butGetClipboard = objc.IBOutlet()
    butPushClipboard = objc.IBOutlet()
    tfXMLEditor = objc.IBOutlet()

    def initialize(self):
        if kwlog:
            print "FMPasteBoxAppDelegate.initialize()"
        userdefaults = NSMutableDictionary.dictionary()
        userdefaults.setObject_forKey_(u"", u'txtFileMakerAppPath')
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


    def applicationDidFinishLaunching_(self, notification):
        app = NSApplication.sharedApplication()
        app.activateIgnoringOtherApps_(True)

        # ugly hack
        wins = app.windows()
        if not wins:
            return
        win = wins[0]
        controller = win.windowController()


    @objc.IBAction
    def getClipboard_(self, sender):
        # pdb.set_trace()
        pasteboardContents = read_pb()
        if not pasteboardContents:
            return
        pbType = pasteboardContents.typ
        pbTypeName = pbType.name
        self.menClipboardtype.setTitle_( pbTypeName )
        self.setTextView_( pasteboardContents.data )


    def setTextView_(self, s):
        # model
        storage = self.tfXMLEditor.textStorage()
        try:
            t = NSMutableAttributedString.alloc().initWithString_(s)
            storage.setAttributedString_( t )
        except Exception, v:
            print
            print "ERROR status inserting:", v


    def textView(self):
        # model
        storage = self.tfXMLEditor.textStorage()
        chars = makeunicode( storage.string() )
        return chars.encode("utf-8")


    @objc.IBAction
    def pushClipboard_(self, sender):
        print "pushClipboard_"

        pasteboard = NSPasteboard.generalPasteboard()
        pasteboard.clearContents()
        data = makeunicode(self.textView())
        data = data.encode("utf-8")
        l = len(data)
        nsdata = NSData.dataWithBytes_length_(data, l)
        pasteboardType = displaynameTypes.get( self.menClipboardtype.title(), u"" )
        if not pasteboardType:
            NSBeep()
            return False
        pasteboardTypeName = pasteboardType.pbname
        pasteboard.setData_forType_( nsdata, pasteboardTypeName)


    @objc.IBAction
    def showPreferencePanel_(self, sender):
        if self.preferenceController == None:
            self.preferenceController = PrefController.alloc().init()
        self.preferenceController.showWindow_( self.preferenceController )



