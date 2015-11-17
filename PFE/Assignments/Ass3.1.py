# PR4E Assignment 3.1
# Michael Hunt
# 11/06/2015

# Pay calculator
# This is Ass2.3 with added allowance for overtime

hrs = raw_input("Enter Hours:")

h=float(hrs)
ot = 0
if hrs > 40 :
    ot = hrs - 40
    h = 40
rate=raw_input("Enter Rate:")
r=float(rate)
pay= h*rate+1.5*ot*r
print pay