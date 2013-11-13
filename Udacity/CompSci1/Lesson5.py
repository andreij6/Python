# Algorithm Analysis

procedure = "well defined sequence of steps that can be executed mechanically "

#Guaranteed to always finish and produce correct result

#-------COST---------



tot = 365 * 700000

estimat = tot + 295000000

one_percent = estimat * .01

#print one_percent

#----------- 

def hash_string(keyword, buckets):
    h = 0
   
    for c in keyword:
        h = ( h+ ord(c) )% buckets
    return h
    
    

#print hash_string('a',12)       #should be 1

#print hash_string('udacity',12) #should be 12

#print hash_string('a', 12)
keyword = "udacity"

#for c in keyword:
#    print c
 
#----------Creating an Empty Hash Table

def make_hashtable(nbuckets):
    i = 0
    table = []
    while i < nbuckets:
        table.append([])
        i = i + 1
    return table

def better_make_hash(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table



def hashtable_get_bucket(htable, key):
    return htable[hash_string(key,len(htable))]

def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable,key).append([key, value])
    return htable

def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None

def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return 
    bucket.append([key, value])
    
    
    