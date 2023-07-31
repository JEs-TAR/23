#prog2 - statistics 

print("O U T P U T\n")

def statistics(l):
    l.sort()
    s = 0
    for i in l:
        s+=i 
    mean = s / len(l)

    d = {}
    m = 0
    for i in set(l):
        g = l.count(i)
        d[i] = g
        if m < g:    
            m=g
    mode = []
    for i in d:
        if d[i] == m:
            mode.append(i)
    
    if len(l)%2 == 0:
        s=(l[(len(l)//2)-1]+l[(len(l)//2)])
        median = s/2
    else:
        median = l[((len(l)+1)//2)-1]

    print("The mean is: {:.2f}".format(mean))
    print("The mode is: ",end="")
    for i in mode:
        print(i,end=" ")
    print()
    print("The median is:",median)

l = eval(input("Enter List: "))
statistics(l)

'''
O U T P U T

Enter List: [1,2,3,3,4]
The mean is: 2.60
The mode is: 3 
The median is: 3

O U T P U T

Enter List: [1,1,3,3]
The mean is: 2.00
The mode is: 1 3
The median is: 2.0
'''