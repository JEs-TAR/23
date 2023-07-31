def palindrome(n):
    if str(n) == str(n)[::-1]:
        return 1
    return -1

def fact(k):
    p = k 
    for i in range(2,k):
        p*=i
    return p

def special(n):
    n = str(n)
    s = 0
    for i in n:
        s+=fact(int(i))
    if s == int(n):
        return 1 
    return -1
