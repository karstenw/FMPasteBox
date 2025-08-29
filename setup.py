"""
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
            "excludes": [
                'TkInter', 'tkinter', 'tk', 'wx', 'sphinx',
                'pyqt5', 'qt5', 'PyQt5', 
                
                'setuptools', 'numba', 
                
                # 'certifi', 'pytz', 
                'notebook', 'nbformat', 'jedi', 'testpath', 'docutils',
                'ipykernel', 'parso', 'Cython', 'sphinx_rtd_theme', 'alabaster',
                'tornado', 'IPython', 'numpydoc', 'nbconvert', 
                'scipy', 'matplotlib', 
                'pandas', 'cv2', 'dlib', 'skimage', 'sklearn', 'mpl_toolkits', 
            ],
        }
    } )

