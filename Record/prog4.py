# prog-4 Binary and reversing

print("O U T P U T\n")

def binary(l):
    x = int(input("Enter Element to be found: "))
    l.sort()
    if x in l:
        s,e = 0 , len(l)-1
        while s <= e:
            mid = (s+e)//2
            if x == l[mid]:
                print("Element found")
                break
            elif x > l[mid]:
                s = mid + 1
            else:
                e = mid - 1
    else:
        print("Element not found!")

while True:
    c = int(input("""1- Binary Search in a list of integers
2-Reversing a string
3-Exit
"""))
    if c == 3:
        print("Bye!")
        break
    elif c ==1:
        n = int(input("Enter Number of terms: "))
        l = []
        for i in range(n):
            l.append(int(input("Enter Integer: ")))
        binary(l)
    elif c ==2:
        s = input("Enter String to be reversed: ")
        print("The reversed string is: ",s[::-1])
    else:
        print("Enter Valid options")


'''
O U T P U T

1- Binary Search in a list of integers
2-Reversing a string
3-Exit
2
Enter String to be reversed: computer
The reversed string is:  retupmoc

1- Binary Search in a list of integers
2-Reversing a string
3-Exit
1
Enter Number of terms: 5
Enter Integer: 1
Enter Integer: 1
Enter Integer: 2
Enter Integer: 4
Enter Integer: 9
Enter Element to be found: 1
Element found

1- Binary Search in a list of integers
2-Reversing a string
3-Exit
3
Bye!
'''