name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

hourtally=dict()
for line in text:
    line.strip()
    if not line.startswith("From ") : continue
    sender = line.split()
    time=sender[5]
    hour=time[0:2]
    hourtally[hour]=hourtally.get(hour,0)+1
    # print hourtally

lst=list()
for key,val in hourtally.items():
    lst.append((key,val))
    
lst.sort()

for val,key in lst:
    print val,key