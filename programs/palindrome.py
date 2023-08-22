"""
WRITE A PROGRAM TO CHECK WHETHER A  NUMBER IS PALINDROME OR NOT
"""
# num = int(input("enter the number:"))
# reverse = int(str(num)[::-1])
# if num == reverse:
#     print("Palindrome")
# else:
#     print("not palindrome")


number = int(input("enter a number:"))
rev = 707
temp = number#707
while number > 0:#707
    rem = number % 10#707%10=7,,70%10=0,7%10=7
    # print(rem)
    rev = (rev*10) + rem#(0*10)+7=7,.....(7*10)+7=707
    number = number // 10#707//10=70...
if temp == rev:
    print("palindrom")
else:
    print("not palindrome")
#
# #
# # num = int(input("enter the number:"))
# # reverse = int(str(num)[::-1])
# # if num ==reverse:
# #     print('palindrome')
# # else:
# #     print("not palindrome")
#
# #fibanocci series
# # #0,1,1,2,3,5,8.............
# # num = 10
# # n1,n2 = 0,1
# # # print(n1)
# # # print(n2)
# # for i in range(num):
# #     print(n1,end=' ')
# #     n3 = n1+n2
# #     n1 = n2
# #     n2 = n3
# #     # print(n3)
#
# amstrong number
# 153 = 1*1*1 + 5*5*5 + 3*3*3 = 153

number = int(input("Enter a number:"))#153 #15 #1
sum = 0
temp = number
while temp > 0:
    n = temp % 10 #153% 10 = 3,  15%10=5  1%10 = 1
    sum = sum + n* n*n #0+3*3*3= 27,27+ 5*5*5=
    temp = temp //10#153//10 = 15
if number == sum:
    print("number is armstrong")
else:
    print("number is not armstrong")
#
# #WAP to print sum of even numbers and sum of odd numbers from given list
# numbers = [3,6,7,5,11,8]


"""

1.	Write a code to reverse a number

2.	Write code of Greatest Common Divisor 

3.	Write code to Check if two strings are Anagram or not

"""


numbers = [3,6,7,5,11,8]
evensum = 0
oddsum = 0
for i in numbers:
    if i % 2 == 0:
        evensum = evensum + i
    else:
        oddsum = oddsum + i
print("sum of even num= ",evensum)
print("sum  od odd numbers= ",oddsum)





# number = int(input("enter the number:"))#707  ,  70, 7
# reverse = 0
# temp = number #707
# while number>0:
#     reminder = number%10 # 707%10 = 7 , 70 % 10 = 0 , 7 %10 = 7
#     reverse = (reverse*10)+reminder # (0*10)+7 = 7 , (7*10)+0 = 70
#     number = number // 10 #707 // 10 = 70  , 70 //10 = 7
#
# if temp==reverse:
#     print("Palindrome")
# else:
#     print("not poalindrome")


#fibanocci series
# 0,1 ,1,2,3,5,8,...........
# num = int(input("enter  the num:"))
# n1,n2 = 0,1
# for i in range(num+1):
#     print(n1)
#     n3 = n1+n2
#     n1 = n2
#     n2 = n3
