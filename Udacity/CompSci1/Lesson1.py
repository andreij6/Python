# Intro to Computer Science Udacity
#-----------Unit 1----------------
'''
    Building a WebCrawler
        writing a program to extract links from websites
        
    Programming
        Procise sequence of steps that turn the computer into anything that we can imagine.       
'''
#Quiz3 
    # the number of minutes in seven weeks
    
print 24 * (7*7) * 60

'''
    Backus-Naur form
        <non-terminal> -> replacement
    
    Derivation - starting from non-terminals and going to a terminal
    
    Expression -> Expression Operator Expression
    Recursive defintion
    Expression -> Number
    Operator -> + , * etc.
    Number -> 0,1,...
    Expression -> (Expression)
'''
#Quiz
# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the variables
# defined below.    

speed_of_light = 299792458   # meters per second
meter = 100                  # one meter is 100 centimeters
nanosecond = 1.0/1000000000  # one billionth of a second

print speed_of_light * meter * nanosecond

#which is always equivelent to the original string s no matter what s is

s = 'ee'
s[:]              #always true
s[:-1]            #false - selection stops before last character
s[0:]             #always true
s + s[0:-1+1]     #s + empty string so this is true
s[:3] + s[3:]     #always true

#----Which of the following evaluate to -1
'test'.find('t')
'test'.find('st')
'Test'.find('te')               #true
'west'.find('test')             #true

#----Which of the following always has the value of 0?
s.find(s)               #true
s.find('s')             #false
's'.find('s')           #true
s.find('')              #true
s.find(s+'!!!')+1       #true because s.find(s+'!!!') evauluats to -1 









