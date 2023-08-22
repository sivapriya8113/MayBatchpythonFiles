"""
1.	Sum all the items in a list
         My_list = [1,2,3,4,5]

"""
# My_list = [1, 2, 3, 4, 5]
# # print(sum(My_list))
# sum = 0 # initial value
# for i in My_list:
#     sum = sum+i #0+1 = 1 ,
#     print(sum)
#
# pdt = 1
# for i in My_list:
#     pdt *=i
#     print(pdt)

# s = ['p', 'y', 't', 'h','o','n']
# str1 = ""
# for i in s:
#     str1 += i
# print(str1)

"""
Write a program to separate negative and positive numbers 
from a given list ?(accept input from the user.)
# """
# A = [1, 7, -8, 6, -5, 2, -4,0]
# x = []
# y = []
# z = []
# for i in A:
#     if i >0:
#         x.append(i)
#         # print(x)
#
#     elif i==0:
#         z.append(i)
#
#     else:
#         y.append(i)
#         # print(y)
#
# print(A)
# print(x)
# print(y)
# print(z)

"""
Write a python program to find largest number in a given list without using max()
My_list = [1, 2, 8,3, 4, 5]

"""
My_list = [1, 2, 8,3, 4, 5]
# My_list.sort(reverse=True)
# print(My_list)
# print(My_list[-1])

max = My_list[0] #1

for i in My_list:
    if i > max:
        max = i
print(max)

name = "priya"
for i in name:
    print(i)
