#prog 10 - Matrix operations

import Matrix as m

print("O U T P U T\n")

while True:
    c = int(input('''1- Swap main and secondary diagonals
2- Sort Row and col
3- Exit
'''))
    if c == 3:
        print('Bye')
        break
    elif c == 1 or c == 2:
        n = int(input("Enter no of rows and col: "))
        matrix = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(int(input("Enter Integer: ")))
                
            matrix.append(temp)

        if c == 1:
            print("The original dict")
            m.printer(matrix)
            print("The modified dict ")
            m.mat(matrix)
        elif c == 2:
            print("The original dict")
            m.printer(matrix)
            print("The modified dict ")
            h = m.sortrowcol(matrix)
            m.printer(h)
    else:
        print(" Invalid option " )
        
