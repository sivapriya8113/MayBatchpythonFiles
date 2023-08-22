row = int(input("enter the num of rows:"))
for i in range(row):
    for j in range(i):
        print(" ",end=" ")
    for k in range(row-i):
        print("*  ",end=" ")
    print()
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(i):
        print("*  ",end=" ")
    print()

