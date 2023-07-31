#prog 8- Nested dict

print("O U T P U T\n")
d = {"SENIORS":{},"JUNIORS":{},"SUBJUNIORS":{}}

for i in d:
    print("Enter points for ",i," Category")
    d[i]["BHARATHI"] = int(input("Enter BHARATHI scores: "))
    d[i]["TAGORE"] = int(input("Enter TAGORE scores: "))
    d[i]["SHIVAJI"] = int(input("Enter SHIVAJI scores: "))
    d[i]["PRATAP"] = int(input("Enter PRATAP scores: "))

def max_score(d):
    for i in d:
        k = [i]
        pts = 0
        for j in d[i]:
            if d[i][j] > pts:
                pts = d[i][j]
                house = j
        k.append(house)
        k.append(pts)
        print(k)
max_score(d)
    
