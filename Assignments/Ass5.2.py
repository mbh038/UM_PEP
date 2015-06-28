
largest = None
smallest = None

while True:
    inp=raw_input("Enter a number: ")

    #Handle the edge cases
    if inp == "done" : break
    if len(inp) <1 : break # check for empty line

    #Do the work
    try :
        num = int(inp)
    except :
        print "Invalid input"
        continue
    
    if smallest is None:
        smallest=num
    elif num < smallest:
        smallest=num
        
    if largest is None:
        largest=num
    elif num > largest:
        largest=num   

print "Maximum is",largest
print "Minimum is",smallest