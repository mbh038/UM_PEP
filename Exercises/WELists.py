fhand=open("mbox-short.txt")
for line in fhand:
    line=line.rstrip()
    print "++",line
    words=line.split()
    print words
    if words[0]!="From": continue
    print "=====",words[2]