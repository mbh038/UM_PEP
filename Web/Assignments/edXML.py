# -*- coding: utf-8 -*-
"""
Created on Sat Dec 05 07:02:59 2015

@author: Mike
"""

import urllib
import xml.etree.ElementTree as ET

#url = 'http://python-data.dr-chuck.net/comments_42.xml'# test
url = 'http://python-data.dr-chuck.net/comments_206667.xml' # assessed  
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
   # print data
#break
tree = ET.fromstring(data)
counts = tree.findall('.//count')
total=0
for count in counts:
    total +=int(count.text)
print total
