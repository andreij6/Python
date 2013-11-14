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

def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    
print fibonacci(15)