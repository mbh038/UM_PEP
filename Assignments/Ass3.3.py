# PR4E Assignment 3.3
# Michael Hunt
# 11/06/2015

# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = raw_input("Enter Score between 0 and 1:")

try :
    score=float(score)
    if score > 1 :
        print "Error. Score must be between 0 and 1 inclusive"
    elif score >= 0.9 :
        print "A"
    elif score >= 0.8 :
        print "B"
    elif score >= 0.7 :
        print "C"
    elif score >= 0.6 :
        print "D"
    elif score >= 0 :
        print "F"
    else :
        print "Error. Score must be between 0 and 1 inclusive"    
except :
    print "Error. Please enter numeric input"