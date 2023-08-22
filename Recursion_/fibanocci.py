# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2) # returns sum of the two previous fib num
# print(fib(5))


#power
"""
# 1. write a recursive function to calculate result of raising a number to a given power 
# 
# eg: 2, 3 = 8 2^3 = 8

2. string palindrome 
"""
# s = input("enter the string:")
# def is_palindrome(s):
#     if len(s) <=1:
#         return True
#     else:
#         if s[0] == s[-1]:
#             return is_palindrome(s[1:-1]) # it excludes the first and last chars
#         else:
#             return False
# print(is_palindrome(s))

# sum_of_digits #n%10 extract last element
n = 234
def sum_of_digits(n):
    if n < 10:

        return n #0
    else:
        # print(n%10 * sum_of_digits(n//10)) #9  #5 #2     #24 #6 #2
        return n%10 * sum_of_digits(n//10)
print(sum_of_digits(n))

