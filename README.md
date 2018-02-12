## FMPasteBox is a OSX FileMaker Clipboard translator. ##


Currently it has only 2 functions:

+ Get the Filemaker clipboard via the "Get Clipboard" button.
  + This loads the xml text into the text field and sets the menu to the received type.
  + The XML can be edited in the app or copy & pasted to any text/xml editor.
  

+ Put the text field contents onto the FileMaker clipboard.
  + This translates the text field back to FileMaker clipboard format. The target format is set by the menu.


A compiled application can be downloaded from my dropbox: [https://goo.gl/3cacFR](https://goo.gl/3cacFR)

FMPasteBox is a Mac apllication written in Python 2.7.14 with PyObjC 4.0.2b1 and py2app 0.15.

It has been tested with FileMaker Pro Advanced 10 & 11 on OSX 10.6 and with FileMaker Pro Advanced 10, 11 & 15 on OSX 10.10.

## Workflow ##

This should work with Filemaker Pro Advanced 10-16; maybe versions 8 & 9 work too.

+ Copy things in Filemaker. Different versions allow different parts to be copy & pasted.

+ Switch to FMPasteBox and press the "Get Clipboard" button. If the FileMaker clipboard is recognized, the test area will hold the XML and the menu will show the type.

+ Edit the XML.

+ press "Push Clipboard". This transfers the XML from the text field back onto the clipboard using the type indicated in the menu.

+ Switch to FileMaker and paste the result.

## A note: ##

The app already has a preferences window in which you can select which Filemaker app to use.  This is __not yet functional__.  Just some preparations for future ideas...


## History ##

2018-02-10 - Version 0.1.0 - First release.
