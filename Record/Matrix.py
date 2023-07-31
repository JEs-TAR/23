
def printer(l):
    n = len(l)
    for i in range(n):
        for j in range(len(l[i])):
            print(l[i][j],end=" ")
        print()

def mat(l):
    n = len(l)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                print(l[i][n-(i+1)],end=" ")
            elif i + j == (n - 1):
                print(l[i][i],end=" ")
            else:
                print(l[i][j],end=" ")
        print()

def bubble(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j]> l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
    

def sortrowcol(l):
    for i in range(len(l)):
        nl = bubble(l[i])
        l[i] = nl
    k = []
    
    for i in range(len(l)):
        z = []
        for j in range(len(l)):
            z.append(l[j][i])
        k.append(z)
    for i in range(len(k)):
        nl = bubble(k[i])
        k[i] = nl
    return k

    
        
        
        
