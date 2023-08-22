n = int(input("Enter the levels you want:"))
k1 = 1

for i in range (n+1):
    for j in range (n-i):   #printing spaces
        print(' ', end = ' ')
    for k in range (i):         #printing characters
        ch = chr(64 + k1)
        print(ch , end='   ')
        k1+= 1                  #iterating characters
    print()
