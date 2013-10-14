#!/usr/bin/env python
variable = 'tutsplus'


def scopeInvestigator():
    global variable
    variable = 'envato'
    print "the variable inside the funtion is", variable    #envato
    
#scopeInvestigator()
#print variable                  #tutspluse when global is set this is envato

#Recursion

def factorial(number):
    if number ==1:
        return 1
    else:
        return number * factorial(number-1)

print "factorial is", factorial(5)
