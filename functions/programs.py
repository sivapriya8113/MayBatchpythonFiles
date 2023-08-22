"""
1.	Multiply all the numbers in a list using function
nums = [7,6,2,3,1]

"""
# nums = [7,6,2,3,1]
# def multiply(nums):
#     mul = 1
#     for i in nums:
#         mul = mul*i
#     return mul
# print(multiply(nums))

"""
3	Write a Python function to calculate the factorial of a number 
(a non-negative integer). The function accepts the number as an argument.
"""

# def factorial(n): #5 5*4*3*2*1
#     fact =1
#     for i in range(1,n+1): #
#         fact =fact*i
#         print(fact)
#     return fact
# n = int(input("enter the  number:"))
# print(factorial(n))
# num = int(input("enter the number :"))
# even = []
# for i in range(4,31):
#      print(i)
#      if i%2==0:
#          even.append(i)
# print(even)

# even = [i for i in range(4,31) if i %2==0]
# print(even)

"""
Generate a Python list of all the even numbers between 4 to 30
"""
#
# def even():
#     even_num = [i for i in range(4,31) if i%2==0]
#     return even_num
#
# print(even())

"""
Write a Python function that takes a number as a parameter and check  the number is prime or not.
"""

#num = int(input("enter the number:"))
# def is_prime(num):
#     if(num<=1):
#         return False
#     for i in range(2,num):
#         if num%i ==0:
#             return False
#     return True
# if(is_prime(num)):
#     print(num,"is a prime number ")
# else:
#     print(num,"is not prime")
#
# def prime_num(a):
#     # flag = False
#     for i in range(2,a):
#         # if a%i ==0:
#             print("a",a%i,i)
#     #         flag = True
#     # if flag == True:
#     #     print('it is not a prime')
#     # else:
#     #     print('prime number')
# num = int(input('enter the number'))
# prime_num(num)


def create_adder(x):
    def adder(y,z):
        return x+y+z
    return adder
print(create_adder(15)(10,50))
# print(add(10,50))

# def mul_num(nums):
#     mul = 1
#     for i in nums:
#         mul = mul*i
#     return mul
# nums = [1,6,7,3,6]
# print(mul_num(nums))
# def mul(a,b,c):
#     return (a*b*c)
# print (mul(2,3,4))
#fibanocci # 0,1 ,1,2,3,5. .

# def fibanocci(n1,n2):
#     for i in range(1,11):
#         print(n1)
#         n3 = n1+n2
#         n1 = n2
#         n2 = n3
# fibanocci(0,1)

# def fib(n1,n2):
#     for i in range(1,11):
#         print(n1)
#         n3 = n1+n2
#         n1 = n2
#         n2 = n3
# fib(0,1)

str1 = "amma"

