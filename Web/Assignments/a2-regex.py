# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re 

fileName="regex_sum_42.txt"
fileName="regex_sum_206665.txt"
sample=open(fileName)
count = []
for line in sample:
    line=line.rstrip()
    #print line
    x=re.findall('[0-9]+',line)
    if len(x)>0:
        x = map(int, x)
        x=sum(x)
        #print x
        count.append(x)
print sum(count)


# Short version
import re
print sum( [ int(i) for i in re.findall('[0-9]+',open("regex_sum_206665.txt").read()) ] )

