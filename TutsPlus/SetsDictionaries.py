#!/usr/bin/env python
#Sets

cars = ['honda','ford','dodge','chevy','honda','dodge']
autos = set(cars)                                           #only returns unique elements  set(['dodge', 'chevy', 'honda', 'ford'])
motorcycles = ['honda','harley','yamaha','bmw','harley']
motos = set(motorcycles)
print motos                                                 #set(['yamaha', 'honda', 'bmw', 'harley'])

print motos - autos                     #set(['harley', 'bmw', 'yamaha'])
print autos | motos                     #set(['dodge', 'yamaha', 'honda', 'ford', 'chevy', 'bmw', 'harley'])
print autos & motos                     #set(['honda'])

#Dictionaries
#unordered collection of key value pairs

web = {'key':'value'}
print web['key']                                                    #value
contact = {'name':'Jesse','location':'Denver','awesome':'yep!'}
print contact['location']                                           #Denver

contact['favorite site'] = 'tutsplus'                               #adds the key and value to a dictionary
del contact['location']
print contact                                                       #Removes key value pair {'favorite site': 'tutsplus', 'awesome': 'yep!', 'name': 'Jesse'}

print contact.keys()                                                #Returns all the keys in a dictionary ['favorite site', 'awesome', 'name']

print 'name' in contact                                             #True
print 'not a real key' in contact                                   #False



