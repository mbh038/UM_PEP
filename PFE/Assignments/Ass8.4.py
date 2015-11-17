fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line=line.rstrip()
    words=line.split()
    
    for w in range(len(words)):
        if words[w] in lst: continue
        lst.append(words[w])
        
lst.sort()
print lst