#prog 5 - List Operations

import random

print("O U T P U T\n")

def generate():
    l = int(input("Enter Lower limit: "))
    u = int(input("Enter Upper limit: "))
    n = int(input("Enter Number of terms: "))

    lis=[]
    for i in range(n):
        k = random.randint(l,u)
        lis.append(k)

    return lis

def max_secmax(l):
    large=l[0]
    
    for i in range(len(l)):
        if l[i]>large:
            large=l[i]
    for i in range(len(l)):
        if l[i]!=large:
            sec=l[i]
            break
    for i in range(len(l)):
        if l[i]!=large and l[1]>sec:
            sec=l[i]

    print("The largest is",large)
    print("The second largest is",sec)


def primes(l):
    prime = []
    for i in range(len(l)):
        h = l[i]
        c = 0
        for j in range(1,h+1):
            if h%j==0:
                c+=1
        if c == 2:
            prime.append(h)
            
    print('The primes generated:',prime)
k = generate()
max_secmax(k)
primes(k)


'''
O U T P U T

Enter Lower limit: 5
Enter Upper limit: 12
Enter Number of terms: 3
The largest is 8
The second largest is 7
The primes generated: [7, 5]

O U T P U T

Enter Lower limit: 4 
Enter Upper limit: 22
Enter Number of terms: 7
The largest is 19
The second largest is 16
The primes generated: [7, 19, 11, 5, 13]
'''
