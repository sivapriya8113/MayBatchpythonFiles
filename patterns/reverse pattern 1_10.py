# levels = int(input("Enter the number: "))#5
#
# for i in range(levels + 1,0,-1): # row
#     for j in range(i - 1, 0, -1):
#         print(j, end='  ')
#     print()

num = int(input("enter the num of rows:"))
for i in range(1,num+1):
    # for j in range(num-1):
    #     print("",end="")
    for k in range(i):
        print(k+1,end=" ")
    print()