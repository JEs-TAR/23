"""
Solution to:
            https://practice.geeksforgeeks.org/problems/61567fb59e9f202db5cc2ad320ffeb6d95bf72d7/1
"""

class Solution:
    def wifiRange(self, N, S, X):
        def looper(current_range):
            for i in range(len(l)):
                if l[i]==1:
                    current_range = X
                    newlist[i] += X+1
                else:
                    if current_range == 0:
                        newlist[i]+=0
                    elif current_range >0:
                        newlist[i]+=current_range
                        current_range-=1
    
            
        l=list(map(int,S))
        newlist = []
        for i in range(len(l)):
            newlist.append(0)
        current_range = 0
        looper(current_range)

        l=l[::-1]
        newlist=newlist[::-1]
        looper(current_range)
        if newlist.count(0) == False:
            return True
        else:
            return
    
"""
This was more efficient for some reason
"""

def wifiRange(self, N, S, X):
    l=list(map(int,S))
    newlist = []
    for i in range(len(l)):
        newlist.append(0)
    current_range = 0
    for i in range(len(l)):
        if l[i]==1:
            current_range = X
            newlist[i] += X+1
        else:
            if current_range == 0:
                newlist[i]+=0
            elif current_range >0:
                newlist[i]+=current_range
                current_range-=1

    l=l[::-1]
    newlist=newlist[::-1]
    for i in range(len(l)):
        if l[i]==1:
            current_range = X
            newlist[i] += X+1
        else:
            if current_range == 0:
                newlist[i]+=0
            elif current_range >0:
                newlist[i]+=current_range
                current_range-=1

    if newlist.count(0) == False:
        return True
    else:
        return False
        

