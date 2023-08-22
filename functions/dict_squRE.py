# num = int(input("enter the number:"))
# dict1 = {}
# for i in range(1,num+1):
#     dict1.setdefault(i,i*i)
# print(dict1)
# n=int(input("enter the nums:"))
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
#
# print (d)

"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""
# num = (input("enter tge number: ").split(','))
# print(num)
# print(tuple(num))


# num = list(map(int,input("enter the nums:").split()))
# print(num)
# print(tuple(num))


"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
import math
from math import sqrt
c = 50
h = 30
sqr = []
num = list(map(int,(input("enter the nums:").split(','))))
for i in num:
    Q = sqrt((2 * c * i) / h)
    sqr.append(int(Q))

print((sqr))
#
