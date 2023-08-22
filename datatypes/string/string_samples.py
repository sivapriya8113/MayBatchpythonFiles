"""
String - Immutable datatype

"""
str1 = "Hello World"
#string indexing
print(str1[0])
print(str1[2])
print(str1[8])
print(str1[-1])

#string slicing
# print(str1[3:8])
# print(str1[::-1])
# print(str1[:-2])
# print(str1[-7::-1])
print(str1[:3])
print(str1[:-1])

str1 = "Hello#World"
# print(str1[-1:-6:-1])
# print(str1[-1:])
#
# print(str1[:4:-1])

print(str1[5::-1])

"""
append new string in the middle of a given string 

s1 = "Python"
s2 = "Luminar" 

o/p: PytLuminarhon

"""
s1 = "Python"
print(len(s1))

s1 = "Python"
s2 = "Luminar"

mid = int(len(s1)/2)
print(mid)
x = s1[:mid]+s2+s1[mid:]
print(x)

"""
create a new string made of the first , 
middle, and last characters of each input string 

s1 = "Python"
s2 = "Luminar"
"""
s1 = "Python"
s2 = "Luminar"
first_char = s1[0] + s2[0]
print(first_char)
mid_chars1 = s1[int(len(s1)/2)] #s1[3]
print(mid_chars1)
mid_chars2 = s2[int(len(s2)/2)] #s2[4]
print(mid_chars2)
mid_char = mid_chars1+mid_chars2
print(mid_char)
last_char = s1[-1]+s2[-1]
print(last_char)
print(first_char+mid_char+last_char)


str1 = "hi dears"
x = str1.replace("hi", "Hello")
print(x)

str2 = " How are you "
print(str1 + str2)

y = (list(str1))
print(y)

z = ''.join(y)
print(z)


