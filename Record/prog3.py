#prog 3 - Factorial and n-fibo

print("O U T P U T\n")

def factorial(n):
    p = 1
    for i in range(2,n+1):
        p*=i
    return p

def fib(n):
    a,b=-1,1
    k = 0
    while k != n:
        c = a+b
        a,b=b,c
        k+=1
        print(c,end=" ")
    print()

while True:
    c = int(input("""1- Factorial
2- Generate ‘N’ numbers of Fibonacci series
3-Exit
"""))
    if c == 3:
        print("Bye!")
        break
    elif c ==1:
        n = int(input("Enter Number to find factorial for: "))
        print("The factorial of",n,"is",factorial(n))
    elif c ==2:
        n = int(input("Enter No. of terms: "))
        fib(n)
                    
    else:
        print("Enter Valid options")
                            
'''
O U T P U T

1- Factorial
2- Generate ‘N’ numbers of Fibonacci series
3-Exit
1
Enter Number to find factorial for: 4
The factorial of 4 is 24

1- Factorial
2- Generate ‘N’ numbers of Fibonacci series
3-Exit
2
Enter No. of terms: 5
0 1 1 2 3

1- Factorial
2- Generate ‘N’ numbers of Fibonacci series
3-Exit
3
Bye!
'''
