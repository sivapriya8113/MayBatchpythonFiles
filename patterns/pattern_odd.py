n = int(input("Enter the levels you want:"))

for count in range (n+1):
    num= 2*count-1
    #print(num)

for i in range (num+1):
    if i%2!=0:
        for j in range (num-i):
            print(' ', end = ' ')
        for j in range (i):
            print('*  ', end=' ')
        print()
