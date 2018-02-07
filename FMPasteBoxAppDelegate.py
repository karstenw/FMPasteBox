#
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

class FMPasteBoxAppDelegate(NSObject):
    menClipboardtype = objc.IBOutlet()

    butGetClipboard = objc.IBOutlet()

    butPushClipboard = objc.IBOutlet()

    def initialize(self):
        if kwlog:
            print "FMPasteBoxAppDelegate.initialize()"
        userdefaults = NSMutableDictionary.dictionary()
        userdefaults.setObject_forKey_(u"", u'txtFileMakerAppPath')
        NSUserDefaults.standardUserDefaults().registerDefaults_(userdefaults)
        self.preferenceController = None

    @objc.IBAction
    def getClipboard_(self, sender):
        print "getClipboard_"


    @objc.IBAction
    def pushClipboard_(self, sender):
        print "pushClipboard_"


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
    def showPreferencePanel_(self, sender):
        if self.preferenceController == None:
            self.preferenceController = PrefController.alloc().init()
        self.preferenceController.showWindow_( self.preferenceController )


