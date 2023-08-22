"""
1. Write a python program to find those numbers
which are divisible by 7 and multiple of 5

2. WAP to find a person can vote or not ..?

4. Traffic light -- if the light is
green -- Car is allowed to go
yellow -- car has to wait
red --- car has to stop


3.  A company decided to give bonus of 5% to employee if his/her
    year of service is more than 5 years.
    Ask user for their salary and year of service and print the net bonus amount.

4. Take three int values from user and print greatest among them

5. A school has following rules for grading system:
    a. Below 25 - F
    b. 25 to 45 - E
    c. 45 to 50 - D
    d. 50 to 60 - C
    e. 60 to 80 - B
    f. Above 80 - A
    Ask user to enter marks and print the corresponding grade.


"""

# num = 35
# if num % 7 ==0 and num % 5 ==0:
#     print("The num is divisible 7 and mul of 5")
# else:
#     print("The num is not divisible 7 and mul of 5")


# age = int(input("enter the age:"))
# if age>=18:
#     print("the person can vote")
# else:
#     print("not eligible")

# year = int(input("enter the year of exp:"))
# salary = int(input("enter the salary:"))
# if year>5:
#     salary = salary+salary*(5/100)#
#     print(salary)
# else:
#     print("not eligible for bonus")


#
# light = input("enter the light:")
# if light=="green":
#     print("Car can go")
# elif light=='Yellow':
#     print("car has to wait")
# elif light=='red':
#     print("car has to stop")
# else:
#     print("Invalid light")
#
#
# # print("----------Program 1-----------")
# # num = int(input("enter the number:"))
# # if num % 7==0 and num % 5 ==0:
# #     print("that num is divisible by 7 and mul of 5")
# # else:
# #     print("that num is not divisible by 7 and mul of 5")
# #
# # #age
# # print("-----Program 2------")
# # age = int(input("enter the age:"))
# # if age>=18:
# #     print("eligible to vote")
# # # else:
# # #     print("not eligible")
#
# print("--------program3----------")
# year = int(input("enter the year of service:"))
# salary = int(input("enter the current salary:"))
# if year>=5:
#     salary = salary+salary*0.05
#     print("bonus = ",salary)
# else:
#     print("Not eligible to get bonus")

# light = input("enter the light:")
# if light=='green':
#     print("Car can go")
# elif light=='yellow':
#     print("Car has to wait")
# elif light=='red':
#     print("car has to stop")
# else:
#     print("Invalig light")


# print("------------Program 5-----------")
# mark = int(input("enter the mark:"))
# if mark < 25:
#     print("Fail")
# elif mark >= 25 and mark < 45:
#     print("Grade E")
# elif mark >= 45 and mark < 50:
#     print("grade D")
# elif mark >= 50 and mark < 60:
#     print("grade C")
# elif mark >= 60 and mark < 80:
#     print("grade B")
# elif mark >= 80:
#     print("Grade A")
# else:
#     print("Invalid grade")

num1 = 0
num2 = 56
num3 = 56

if num1 >= num2 and num1 >= num3:
    print("Largest is ",num1)
elif num2 >= num3 and num2 >= num1:
    print(num2,"num2 is greater")
else:
    print(num3,"num3 is greater")

