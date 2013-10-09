#!/usr/bin/env python
listed = ['the','holy','grail']
print listed
nested_listed = ['the','monty','python','and',listed]
print nested_listed
#testing for membership
print 'monty' in nested_listed      #true
print 'holy' in nested_listed       #false

print nested_listed[1]              #monty
print nested_listed[-1]             #list ['the', 'holy','grail']

print nested_listed[-1][1]          #holy

print nested_listed[0:2]            #'the' 'monty'
print nested_listed[2:-2]           #'python'

#lists are mutable

nested_listed[1]='awesome'
print nested_listed                 #['the', 'awesome', 'python', 'and', ['the', 'holy', 'grail']]
nested_listed[-1:] = ['tuts','plus']
print nested_listed                 #['the', 'awesome', 'python', 'and', 'tuts', 'plus']

#list methods (check out the python doc for more

nested_listed.append('for sure')
print nested_listed                 #['the', 'awesome', 'python', 'and', 'tuts', 'plus', 'for sure']
nested_listed.insert(1,'super')
print nested_listed                 #['the', 'super', 'awesome', 'python', 'and', 'tuts', 'plus', 'for sure']

another_list = ['python', 'rocks']
nested_listed.extend(another_list)  
print nested_listed                 #['the', 'super', 'awesome', 'python', 'and', 'tuts', 'plus', 'for sure', 'python', 'rocks']
    
nested_listed.remove('awesome')

#Tuple they are immutable  -- does not support item assignment

tupled = 'one','two','three'        # print tupled   ('one', 'two', 'three')
tupled[1]                           #two
tupled[:2]                           #'one','two'
tupled[1:]                           #'two','three'
tuple2 = 'tuts','plus'
tuple3 = tuple2,tupled              #(('tuts', 'plus'), ('one', 'two', 'three'))





                    




