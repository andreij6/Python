#!/usr/bin/env python
name = raw_input('Please type in your name: ')

if len(name) < 5:
    print "Your name has fewer than 5 characters"
elif len(name) == 5:
    print "Your name has exactly 5 characters"
    if name == "Andre":
        print "Hey You!!"
else:
    print "Your name has greater than 5 characters"
    
'''    
if len(name) <= 5:
    print "Your name has fewer than or equal to 5 characters"
    
if len(name) != 5:
    print "Your name does not have five characters"
    
'''
    
language = raw_input('Please enter a programming language: ')

if language in ['C++','Python','Java']:
    print language, "rocks"
    
if language not in ['C++','Python','Java']:
    print language, "is just ok"
    
dinner = raw_input('Please choose a pizza or spaghetti: ')

if dinner == "pizza" or dinner == "spaghetti":
    print 'bon appetit'
else:
    print "You can't have", dinner, "for dinner"