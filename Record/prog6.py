#prog 6- BMI and Vowels MDC

print("O U T P U T\n")

def vow():
    t = ()
    for i in range(int(input("Enter No of strings: "))):
        s = input("Enter String: ")
        t+=(s,)
    ans = ()
    v = "aeiouAEIOU"
    for i in t:
        c = 0
        for j in v:
            if j in set(i):
                c+=1
        if c ==5:
            ans+=(i,)
    return ans

def bmi():
    t = ()
    n = int(input("Enter Number of persons: "))
    for i in range(n):
        h = int(input("Enter Height (m): "))
        w = int(input("Enter Weight (m): "))
        temp = (h,w)
        t+=(temp,)

    for i in t:
        height = i[0]
        weight = i[1]
        bmi_ = weight/(height**2)
        if bmi_ < 18.5:
            status = "underweight"
        elif bmi_ > 18.5 and bmi_ <= 25:
            status = "Normal"
        elif bmi_ > 25 and bmi_ < 30:
            status = "Overweight"
        elif bmi_ > 30:
            status = "Obese"
        print({"BMI":bmi_,"Category":status})
            
    
        
while True:
    x = int(input("""1) Display words with all vowels
2) Check BMI
3) Exit
"""))
    if x == 3:
        print("Bye!")
        break
    elif x == 1:
        print(vow())
    elif x == 2:
        bmi()
    elif x == 3:
        print("Byee")
        break
    else:
        print("Invalid Option")        
            
