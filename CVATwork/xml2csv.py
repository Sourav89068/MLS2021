import xml.etree.ElementTree as ET
import pandas as pd
import csv

def xml2csv(xmlfile):
    tree=ET.parse(xmlfile)
    a={}
    n=len(tree.findall('track')[0])
    frame=[int(tree.findall('track')[0][i].attrib['frame'])+1 for i in range(n)]
    lef=[float(tree.findall('track')[0][i].attrib['xtl']) for i in range(n)]
    to=[float(tree.findall('track')[0][i].attrib['ytl']) for i in range(n)]
    ri=[float(tree.findall('track')[0][i].attrib['xbr']) for i in range(n)]
    bo=[float(tree.findall('track')[0][i].attrib['ybr']) for i in range(n)]
    a={'frameno':frame,'left':lef,'top':to,'right':ri,'bottom':bo}
    dat=pd.DataFrame(a)
    return dat.to_csv('track.csv',index=False)