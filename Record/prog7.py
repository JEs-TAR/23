#prog 7- Dict MDC subscribers 

print("O U T P U T\n")
def add():
    name = input("Enter Subscriber Name: ")
    ph = input("Enter Phone Number: ")
    d[ph] = name

def view():
    print(d)

def modify():
        num = input("Enter Phone Number of subscriber: ")
        if num in d:
            print("The Current Name is: ",d[num])
            name = input("Enter New Name: ")
            d[num] = name
        else:
            print("No number found!")
def delete():
    num = input("Enter Phone Number to be deleted: ")
    if num in d:
        d.pop(num)
    else:
        print("No number found!")
d = {}

while True:
    choice = int(input("""1. ADD
2. VIEW
3. MODIFY NAME
4. DELETE
5. EXIT"""))
    if choice == 5:
        print("Byee!")
        break
    elif choice == 1:
        add()    
    elif choice == 2:
        view()
    elif choice == 3:
        modify()
    elif choice == 4:
        delete()
    else:
        print("Invalid Option")