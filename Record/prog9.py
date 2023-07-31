#prog 9- User defined module

import Number as n
print("O U T P U T\n")

while True:
    choice = int(input("""1- Palindrome Numbers in a list
2- Special Numbers in a given range
3- Exit
""" ))
    if choice == 3:
        print("Bye!")
        break 
    elif choice == 1:
        N = int(input("Enter Number of elements: "))
        l = []
        for i in range(N):
            l.append(int(input("Enter Integer: ")))
        result = []
        for i in l:
            if n.palindrome(i) == 1:
                result.append(i)
        if result:
            print(result," are the palindrome Numbers!")
        else:
            print("No such numbers found!")
    elif choice == 2:
        l = int(input("Enter Lower limit: "))
        u = int(input("Enter Upper limit: "))
        result = []
        for i in range(l,u+1):
            if n.special(i) == 1:
                result.append(i)
        if result:
            print(result," are the special numbers in given range!")
        else:
            print("No such numbers in given range")
    else:
        print("Invalid option")
    
