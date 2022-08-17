#
#   FMPasteBoxPreferenceController.py
#
#   Created by Karsten Wolf on 07.02.18.
#   Copyright 2018 Karsten Wolf. All rights reserved.
#


from __future__ import print_function

import objc

import Foundation
NSUserDefaults = Foundation.NSUserDefaults


import AppKit
NSApplication = AppKit.NSApplication
NSWindowController = AppKit.NSWindowController

import FMPasteBoxTools



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

class FMPasteBoxPreferenceController (NSWindowController):

    butSetFileMakerAppPath = objc.IBOutlet()
    butSetExportsPath = objc.IBOutlet()

    cbDoExports = objc.IBOutlet()

    txtFileMakerAppPath = objc.IBOutlet()
    txtExportsPath = objc.IBOutlet()

    def init(self):
        self = self.initWithWindowNibName_("Preferences")

        wnd = self.window()
        wnd.setTitle_( u"FMPasteBox Preferences" )
        wnd.setDelegate_( self )

        defaults = NSUserDefaults.standardUserDefaults()
        self.txtFileMakerAppPath.setStringValue_( defaults.objectForKey_( u'txtFileMakerAppPath') )
        self.txtExportsPath.setStringValue_( defaults.objectForKey_( u'txtExportsPath') )
        self.cbDoExports.setState_( defaults.objectForKey_( u'cbDoExports') )
        return self


    def windowWillClose_(self, notification):
        defaults = NSUserDefaults.standardUserDefaults()
        defaults.setObject_forKey_(self.txtFileMakerAppPath.stringValue(),   u'txtFileMakerAppPath')
        defaults.setObject_forKey_(self.txtExportsPath.stringValue(),   u'txtExportsPath')
        defaults.setObject_forKey_(self.cbDoExports.state(),   u'cbDoExports')


    @objc.IBAction
    def chooseFolder_(self, sender):
        if sender == self.butSetFileMakerAppPath:
            folders = FMPasteBoxTools.getApplicationDialog()
            if folders:
                self.txtFileMakerAppPath.setStringValue_( folders )
        elif sender == self.butSetExportsPath:
            folders = FMPasteBoxTools.getFolderDialog()
            if folders:
                self.txtExportsPath.setStringValue_( folders[0] )



