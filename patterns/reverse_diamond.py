n = int(input("Enter the levels you want:"))

for i in range (n,0,-1):
    for j in range (n-i):
        print(' ', end = ' ')
    for j in range (i):
        print('*  ', end=' ')
    print()
for i in range (n+1):
    if i>0:
        for j in range (1,n-i+1):
            print(' ', end = ' ')
        for j in range (1,i+1):
            print('*  ', end=' ')
        print()
