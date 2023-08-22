# """
# Function
# --------
#
# A function is a block of code which only runs when it is callled ,
#
# A function can return a data as a result.
#
#
# return ---
#
# syntax
#
# :parameter
#
# :argument
#
# """
#
# def sum():
#     a = 6
#     b = 7
#     c = a+b
#     print(c)
# sum()
# sum()
#
# def sum(a,b):
#     c = a+b
#     return c
# print(sum(5,6))
#
# #sum of n natural numbers
# num = int(input("enter the number:"))
# sum = 0
# for i in range(num+1):
#     sum = sum+i
# print(sum)
#
# #
# def sum_naturals(num):
#     sum = 0
#     for i in range(num+1):
#         sum = sum+i
#     return sum
# num = int(input("enter the bnumber:"))
# print(sum_naturals(num))
# #
# #
#
# # def sum1():
# #     a = 6
# #     b= 7
# #     c = a+b
# #     print(c)
# # sum1()
# #
# # def sum2(a,b):
# #     return a+b
# # print(sum2(6,7))
# # sum1()
# # print(sum2(8,7))#
# # #
# # #
# def sumOfNnums(num):
#      s = 0
#      for i in range(1,num+1):
#          s = s+i
#      return s
# num = int(input("enter the range of nums:"))
# print((sumOfNnums(num)))
#
# num1 = 34
# num2 = 67
# num3 = 89
#
# def max():
#     if num1>num2 and num1>num3:
#         return num1
#     elif num2>num1 and num2>num3:
#         return num2
#     else:
#         return num3
# print(max())
#
#
# #to find the sum of list of numbers
#
#
# numbers = [1,2,3,4,7,8]
# def sum_of_list(numbers):
#     # global name
#     name = 'priya'
#     global sum
#     sum = 0
#     for i in numbers:
#         sum = sum+i
#     return sum
# print(sum_of_list(numbers))
# print(sum)
#

# def myfunc():
#   def myinnerfunc():
#     global x
#     x = 300
#     print(x)
#   myinnerfunc()
#
# myfunc()
# print(x)
# #

#
# num = [6,8,5,3,2,1]
# def sum_list(num):
#   sum=0
#   for i in num:
#     sum = sum+i
#   return sum
# print(sum_list(num))

# str1 = "Python"
def laptop(name,model,color):
    print("laptop details:",name,model,color)
laptop('Dell','i5','grey')

def student(**kwargs): # Arbitary keyword arguments
    print("student details",kwargs['name'],kwargs['ids'],kwargs['course'])
student(name='priya',ids = 12, course='python', place='asdd')


def names(*args): #arbitary arguments
    print("names:",args)
names('shamsa','ajnas','priya','dfg')


def keyword(child1,child2,child3): #keyword argument
    print("the yougest child is "+child3)
keyword(child2='Jin',child3='Jack', child1='Jain')

def country(country='India'):
    print("i'm from "+country)
country()
country('Itali')
country('USA')



# string = 'python'
# s = list(string)
# print(s)
# s.reverse()
# print(s)
# print(''.join(s))

# def reverse(string):
#     s = list(string)
#     s.reverse()
#     print(''.join(s))
#
# string = 'python'
# reverse(string)
# reverse(string)

# def reverse(string):
#     s = ''
#     for i in string:
#         s = i+s
#         print(s)
# string = 'python'
# reverse(string)

str = 'python'
# print(str[-1])
string = [str[i] for i in range(len(str)-1,-1,-1) ]
print(''.join(string))



