# n = int(input("Enter the levels you want:"))
# k=1
# #ch = chr(64+k) #getting alphabet
#
# for i in range (n+1):
#     for j in range (i):
#         #print(j)
#         ch = chr(64 + k)  # iterating alphabets
#         print(ch, end=' ') #printing variables
#         k+= 1
#     print()

# ascci_number = 65
# rows = int(input("enter the num of rows: "))
# for i in range(0,rows):
#     for j in range(0,i+1):
#         char = chr(ascci_number)
#         print(char,end=' ')
#         ascci_number += 1
#     print(" ")


# num = int(input("enter the num of rows:"))#5
# k = 1
# for i in range(1,num):#rows
#     for j in range(i):#col
#         print(chr(64+k),end=" ")
#         k+=1
#     print()

# num = int(input("enter the num of rows:"))
# for i in range(65,65+num):
#     # print(i)
#     for j in range(65,i+1):#(65,66)(65,67)(65,68).........
#           # print(j)
#         print(chr(j),end=" ")
#     print()

num = int(input("enter the num of rows:"))#5
Y = 1
for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end=" ")
    for k in range(i):
        print(chr(64+Y),end="   ")
        Y+=1
    print()

print(ord('A'))