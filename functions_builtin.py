"""
# map , filter reduce
# map(function,iterable)
# filter(function,iterable)
from functools import reduce

# """
from functools import reduce

#
# # from functools import reduce
#
# items = [1,2,3,4]
#
# # def testfin():
# #     sqr = []
# #     for i in items:
# #         sqr.append(i**2)
# #     print(sqr)
# #
# # testfin()
#
# # sqr = [i**2 for i in items]
# # print(sqr)
# items = [1,2,3,4]
# sqr = list(map(lambda x: x**2,items))
# print(sqr)

# # def sqr():
# #     for i in items:
#
#
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

# result = map(lambda x, y: x * y, numbers1, numbers2)
# print(list(result))
#
# filter
# numbers = [-3,-6,-5,2,5,6,-2]
# less_than_zero = list(filter(lambda x:x<0,numbers))
# print(less_than_zero)

# #reduce
#
# product = 1
# list1 = [1,5,4,6]
# for num in list1:
#     product = product * num
# print(product)
# #
list1 = [1,5,4,6]
product = reduce((lambda x,y:x*y),list1)
print(product)
# #
# num = int(input("enter the number:"))
# sum = reduce(lambda x,y : x+y,range(num+1))
# print(sum)

#
#
#
# """
# Exam
# ----
# 1. To find the sum of n natural numbers
# 2.
#
# """
# n =int(input("enter a number:"))
# for i in range (n):
#     for j in range(n-i):
#         print(' ',end='')
#     for k in range (i+1):
#         print("*",end=' ')
#     print()


# n=int(input("enetr the rows:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end=' ')
#     for k in range(i):
#         print(' * ',end=(' '))
#     print()


# def func_name():
#     print("Hi dears")
# func_name()
# func_name()
# func_name()

# def sum(a,b):
#     c = a+b
#     Y = a*b
#     print(c)
#     print(Y)
# sum(5,4)
#
# x = lambda a,b:a+b
# print(x(5,4))

# nums = [1,5,3,4]
# sqr = []
# for i in nums:
#     sqr.append(i**2)
# print(sqr)
#
# sqr = [i**2 for i in nums]
# print(sqr)
#
# sqr = list(map(lambda x:x**2,nums))
# print(sqr)

# def even(number):
#          if number%2==0:
#              return True
#          return False
#
# numbers = [1,5,2,4,6,8]
# even_nums  = list(filter(even,numbers))
# print(even_nums)

# numbers = [1,5,2,4,6,8]
# def even(numbers):
#     even_num =[]
#     for i in numbers:
#         if i%2 ==0:
#             print(even_n
#             um.append(i))
#     return even_num
# print(even(numbers))



# count = 0
# while(True):
#    if count % 3 == 0:
#        print(count, end = " ")
#    if(count > 15):
#        break
#    count += 1

#
# def solve(a):
#    a = [1, 3, 5]
# a = [2, 4, 6]
# print(a)
# solve(a)
# print(a)


