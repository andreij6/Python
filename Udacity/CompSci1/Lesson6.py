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
