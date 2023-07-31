#prog 1 - UDF Series

print("O U T P U T\n")

x = int(input("Enter X: "))
n = int(input("Enter No of Terms: "))
S = int(input("Series Number: "))

def fact(k):
    p = 1
    for i in range(2,k+1):
        p*=i
    return p

def series(x,n,s):
    S = 0
    for i in range(1,n+1):
        if s == 1:
            nr = x**((2*i)-1)
            dr = fact(2*i)*((-1)**(i+1))
            S+=(nr/dr)
        elif s == 2:
            nr = x ** ((2*i)-1)
            dr = fact((2*i)+1)*((-1)**(i+1))
            S+=(nr/dr)
    return S

print(series(x,n,S))


'''
O U T P U T

Enter X: 2
Enter No of Terms: 2
Series Number: 1
0.6666666666666667

O U T P U T

Enter X: 1
Enter No of Terms: 4
Series Number: 2
0.15852899029982362
'''