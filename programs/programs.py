"""
1. to check whether a number is prime or not

"""

# num = int(input("Enter the number:"))
# flag = False
# for i in range(2,num):
#     if num % i == 0:
#         flag = True
#         break
# if flag == True:
#     print(num,"not prime ")
# else:
#     print(num,"the num is prime ")
# #
# for i in range(1,15):
#     print(i)


num = int(input("Enter the number:"))
if num<1:
    for i in range(2,num):
        if num % i ==0:
            print(num,"not prime")
            break
        else:
            print(num,"is  prime")
else:
    print(num," is not prime ")
# else:
#     print(num,"is not prime")
