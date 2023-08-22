n = int(input("Enter the levels you want:"))

for i in range (n+1):
    for j in range (i,0,-1):
        print(chr(ord('A')+j-1), end='  ')

    print()
