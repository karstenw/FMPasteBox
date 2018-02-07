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

import AppKit
NSWindowController = AppKit.NSWindowController
NSApplication = AppKit.NSApplication
NSUserDefaults = AppKit.NSUserDefaults
NSMutableAttributedString = AppKit.NSMutableAttributedString

import FMPasteBoxTools
read_pb = FMPasteBoxTools.read_pb
write_pb = FMPasteBoxTools.write_pb
fmpPasteboardTypes = FMPasteBoxTools.fmpPasteboardTypes
additionalFMPPasteboardTypes = FMPasteBoxTools.additionalFMPPasteboardTypes

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
        defaults = NSUserDefaults.standardUserDefaults()

        self.menClipboardtype.removeAllItems()
        menuItems = [ u"" ]
        for pbTypeName in fmpPasteboardTypes:
            pbType = fmpPasteboardTypes[pbTypeName]
            menuItems.append( pbType.name )
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


    @objc.IBAction
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


    @objc.IBAction
    def showPreferencePanel_(self, sender):
        if self.preferenceController == None:
            self.preferenceController = PrefController.alloc().init()
        self.preferenceController.showWindow_( self.preferenceController )



