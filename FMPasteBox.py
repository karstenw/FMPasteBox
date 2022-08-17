#
#  FMPasteBox.py
#  FMPasteBox
#

from __future__ import print_function

import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

import FMPasteBoxAppDelegate


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

if __name__ == '__main__':
    AppHelper.runEventLoop()

