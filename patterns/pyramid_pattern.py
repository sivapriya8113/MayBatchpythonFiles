n = int(input("Enter the levels you want:"))  # 5

for i in range(1, n + 1):  # rows 1,.... 5
    for j in range(n - i):
        # print(j)
        print(' ', end=' ')
    for k in range(i): #0, 0,1, 0,1,2...
        print(k, end='   ')

    print()

#
# n = int(input("Enter the levels you want:")) #5
#
# for i in range (n+1):#rows 1,.... 5
#         for j in range(i): #space #5-1=4, 5-2 = 3,
#             print(' ', end = '')
#         for k in range (n-i):
#             print('* ', end='')
#         print()
