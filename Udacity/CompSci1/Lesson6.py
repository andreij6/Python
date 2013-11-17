def factorial(n):
    if n == 0:          #BASECASE
        return 1
    else:
        return n*factorial(n-1)
    
print factorial(3)

def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
        
def iter_palindrome(s):
    for i in range(0, len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def fibonacci(n):                               #    Recursive                                            
                                                #    Takes a long time for higher numbers
    if n==0 or n==1:                            #    Not effiecient doing redundant work           
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    

def while_fibonacci(n):                             #    Iteratively
    current =   0 
    after   =   1
    for i in range(0, n):
        current, after = after, current + after     #    Multiple assignment
    return current

print while_fibonacci(33)

mass_of_earth   = 5.9722 * 10**24
mass_of_rabbit  = 2

n = 1

while while_fibonacci(n) * mass_of_rabbit < mass_of_earth:
    n = n+1
print n, while_fibonacci(n)

#Relaxation Algorithm
#Start with a guess 
#while not done:
#      make the guess better

def popularity(t,p):
    if t == 0:
        return 1
    else:
        score = 0
        for f in friends(p):
            score = score + popularity(t-1,f)
        return score
        
def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            
            for node in graph:              
                if page in graph[node]:                                         #if page is in that list
                    newrank = newrank + d * (ranks[node] / len(graph[node]))    #
            newranks[page] = newrank
        ranks = newranks
    return ranks