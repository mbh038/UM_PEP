# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

#import urllib
##from BeautifulSoup import *
#from bs4 import BeautifulSoup
#
#url = raw_input('Enter URL - ')
#count=int(raw_input('Count - '))
#pos = int(raw_input('Position - '))
#html = urllib.urlopen(url).read()
#
#soup = BeautifulSoup(html)

## Retrieve all of the anchor tags
#tags = soup('span')
#counts=0
#for tag in tags:
#    # Look at the parts of a tag
#    print 'TAG:',tag
#    print 'URL:',tag.get('href', None)
#    print 'Contents:',tag.contents[0]
#    print 'Attrs:',tag.attrs
#    counts +=int(tag.contents[0])
#    
#print "sum: ",counts

import urllib
#from BeautifulSoup import *
from bs4 import BeautifulSoup

url = raw_input('Enter URL - ')
count=int(raw_input('Count - '))
pos = int(raw_input('Position - '))
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

for i in range(count):
    tags = soup('a')
    nextUrl=tags[pos-1].get('href', None)
    #print nextUrl
    #urllib.urlopen(tags[pos-1].get('href', None)).read()
    #print nextUrl
    nextHtml = urllib.urlopen(nextUrl).read()
    soup = BeautifulSoup(nextHtml)
    print tags[pos-1].contents[0]    
