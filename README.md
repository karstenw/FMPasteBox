## FMPasteBox is a OSX FileMaker Clipboard translator. ##


Currently it has only 2 functions:

+ Get the Filemaker clipboard via the "Get Clipboard" button.
  + This loads the xml text into the text field and sets the menu to the received type.
  + The XML can be edited in the app or copy & pasted to any text/xml editor.
  

+ Put the text field contents onto the FileMaker clipboard.
  + This translates the text field back to FileMaker clipboard format. The target format is set by the menu.

If the "Export pasteboard to folder" preference is activated and the "Export Folder" pref points to a valid folder, all "Get Clipboard" actions are logged exported into that folder. If the pasteboard content is any of the layout types, additional exports are done depending on the FileMaker version used.


A compiled application can be downloaded from my dropbox: [https://goo.gl/3cacFR](https://goo.gl/3cacFR)

FMPasteBox is a Mac apllication written in Python 2.7.14 with PyObjC 4.0.2b1 and py2app 0.15.

It has been tested with FileMaker Pro Advanced 10 & 11 on OSX 10.6 and with FileMaker Pro Advanced 10, 11 & 15 on OSX 10.10.

## Workflow ##

This should work with Filemaker Pro Advanced 10-16; maybe versions 8 & 9 work too.

+ Copy things in Filemaker. Different versions allow different parts to be copy & pasted. Layout objects should work in all versions.

+ Switch to FMPasteBox and press the "Get Clipboard" button. If the FileMaker clipboard is recognized, the text view will hold the XML and the menu will show the type.

+ Edit the XML.

+ press "Push Clipboard". This transfers the XML from the text field back onto the clipboard using the type indicated in the menu.

+ Switch to FileMaker and paste the result.

+ If you activated the "Export pasteboard to folder" preference and assigned a folder to it, all XML and additional pasteboard content will be written to disk. Go explore.



## History ##

2022-08-17 - Version 0.4.0 - Move to Python3.8

2018-02-27 - Version 0.3.2 - Hid and deactivated unused FileMaker preference.

2018-02-27 - Version 0.3.1 - Minor corrections & fixes.

2018-02-26 - Version 0.3.0 - Added Layout asset and CSS exports.

2018-02-18 - Version 0.2.0 - Added Export preferences. Exported are the XML files and additional formats (PDF, TIFF, JPG, PICT) if present for layout objects.

2018-02-12 - Version 0.1.1 - Fixed a bug where "Push Clipboard" would destroy the clipboard even if there was nothing to push.

2018-02-10 - Version 0.1.0 - First release.
