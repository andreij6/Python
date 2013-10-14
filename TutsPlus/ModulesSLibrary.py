#!usr/bin/env python

#import sys
#from sys import argv
#print argv

import re

print re.search('a(.*)e', 'apple').group()
print re.search('a(.*)e', 'applebum').group()
print re.search('a(.*)e', 'apple').group(1)
print re.findall('\w+@\w+\.com','email1 is jess@email.com email2 is bob@makers.com')


