#
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



class FMPasteBoxPreferenceController (NSWindowController):

    butSetFileMakerAppPath = objc.IBOutlet()

    txtFileMakerAppPath = objc.IBOutlet()

    def init(self):
        self = self.initWithWindowNibName_("Preferences")

        wnd = self.window()
        wnd.setTitle_( u"FMPasteBox Preferences" )
        wnd.setDelegate_( self )

        defaults = NSUserDefaults.standardUserDefaults()
        self.txtFileMakerAppPath.setStringValue_( defaults.objectForKey_( u'txtFileMakerAppPath') )
        return self


    def windowWillClose_(self, notification):
        defaults = NSUserDefaults.standardUserDefaults()
        defaults.setObject_forKey_(self.txtFileMakerAppPath.stringValue(),   u'txtFileMakerAppPath')



    @objc.IBAction
    def chooseFolder_(self, sender):
        if sender == self.butSetFileMakerAppPath:
            folders = FMPasteBoxTools.getApplicationDialog()
            if folders:
                self.txtFileMakerAppPath.setStringValue_( folders )



