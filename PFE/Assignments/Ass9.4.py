name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

people=dict()
for line in text:
    line.strip()
    if not line.startswith("From ") : continue
    sender = line.split()
    people[sender[1]]=people.get(sender[1],0)+1

max=-1
for key in people :
    if people[key]>max:
        max=people[key]
        keymax=key
        
print keymax,max