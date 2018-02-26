import sys
import os

import binascii
import base64
import hashlib

import xml.etree.cElementTree
ElementTree = xml.etree.cElementTree
import xml.parsers.expat

import pdb

import FMPasteBoxTools
makeunicode = FMPasteBoxTools.makeunicode


def stringhash( s ):
    m = hashlib.sha1()
    m.update(s)
    return m.hexdigest().upper()



g_CSSCollector = {}

def exportAssets( xmlpath, exportfolder ):
    global g_CSSCollector
    g_CSSCollector = {}
    
    assetfolder = os.path.join( exportfolder, 'Assets')
    cssfolder = os.path.join( exportfolder, 'CSS')
    
    # parse xml file
    try:
        basenode = ElementTree.parse( xmlpath )
    except  (xml.parsers.expat.ExpatError, SyntaxError), v:
        xml.parsers.expat.error()
        print u"EXCEPTION: '%s'" % v
        print u"Failed parsing '%s'\n" % xmlpath
        return

    idx = 1
    for laynode in basenode.getiterator ( "Layout" ):
        for l in laynode.getchildren():
            t = l.tag
            if t == u'Object':
                idx = get_layout_object( l, assetfolder, idx+1)

    print idx, "Object nodes"
    # write out CSS
    exportfolder = os.path.join( exportfolder, "CSS")
    for k in g_CSSCollector:
        css = g_CSSCollector[k]
        foldername = "%s %s" % (str(css.objectcount).rjust(3, '0'), css.themename)
        folder = os.path.join( exportfolder, foldername)
        if not os.path.exists( folder ):
            os.makedirs( folder )
        path = os.path.join( folder, "local.css")
        f = open(path, 'w')
        f.write(css.localcss)
        f.close()
        path = os.path.join( folder, "full.css")
        f = open(path, 'w')
        f.write(css.fullcss)
        f.close()


def get_layout_object(laynode, exportfolder, objectcount):
    nodes = list(laynode)
    extensions = dict(zip( ("JPEG","PDF ", "PNGf", "PICT",
                            "GIFf", "8BPS", "BMPf"),
                           (".jpg",".pdf", ".png", ".pict",
                            ".gif", ".psd", ".bmp")))
    exttypelist = extensions.keys()

    for node in nodes:
        cur_tag = node.tag

        if cur_tag == u'Object':
            # get layout object
            objectcount = get_layout_object(node, exportfolder, objectcount+1)

        elif cur_tag == u'GraphicObj':
            for grobnode in node:
                if grobnode.tag == "Stream":
                    stype = []
                    sdata = ""
                    for streamnode in grobnode:
                        streamtag = streamnode.tag
                        streamtext = streamnode.text
                        if streamtag == "Type":
                            if streamtext not in exttypelist:
                                stype.append( '.' + streamtext )
                            else:
                                stype.append( streamtext )
                        elif streamtag in ("Data", "HexData"):
                            if not stype:
                                continue
                            curtype = stype[-1]
                            ext = extensions.get( curtype, False )
                            if not ext:
                                ext = curtype
                            if ext in ('.FNAM', '.SIZE', '.FORK'):
                                continue
                            data = None
                            if streamtag == "HexData":
                                try:
                                    data = binascii.unhexlify ( streamtext )
                                except TypeError, err:
                                    pass
                            elif streamtag == "Data":
                                try:
                                    data = base64.b64decode( streamtext )
                                except TypeError, err:
                                    pass
                            if not data:
                                continue

                            #fn = (str(objectcount).rjust(5, '0')
                            #        + '-'
                            #        + stringhash( data ))
                            fn = stringhash( data )
                            if not os.path.exists( exportfolder ):
                                os.makedirs( exportfolder )

                            path = os.path.join(exportfolder, fn + ext)

                            # write Asset file
                            if not os.path.exists( path ):
                                f = open(path, "wb")
                                f.write( data )
                                f.close()
                        elif streamtag == "Styles":
                            objectcount = dostyles(streamnode, exportfolder, objectcount)

        elif cur_tag == u'GroupButtonObj':
            # recurse
            objectcount = get_layout_object(node, exportfolder, objectcount)

        elif cur_tag == u'FieldObj':
            pass

        elif cur_tag == u'Step':
            pass

        elif cur_tag == u'TextObj':
            pass

        elif cur_tag == u'ObjectStyle':
            continue
    
        elif cur_tag == u'Table':
            pass

        elif cur_tag == u'Styles':
            objectcount = dostyles(node, exportfolder, objectcount)
    return objectcount


class CSSCollector:
    def __init__(self, objectcount):
        self.objectcount = objectcount
        self.localcss = ""
        self.fullcss = ""
        self.themename = ""
        self.hash = ""


def dostyles( node, exportfolder, objectcount ):
    nodes = list(node)
    css = CSSCollector(objectcount)
    if objectcount == 64:
        pdb.set_trace()

    for node in nodes:
        cur_tag = node.tag

        if cur_tag == u'LocalCSS':
            css.localcss = node.text
        elif cur_tag == u'FullCSS':
            css.fullcss = node.text
        elif cur_tag == u'ThemeName':
            css.themename = node.text

    data = css.themename + css.localcss + css.fullcss
    if not data:
        return objectcount
    css.hash = stringhash( css.localcss + css.fullcss )
    g_CSSCollector[css.hash] = css
    return objectcount





