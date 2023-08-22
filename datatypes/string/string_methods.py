str1 = "Hello world"
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print()

"""
upper()
lower()
capitalize()
find()
join()
split()
"""

list1 = ["apple","orange","banana"]
x = ''.join(list1)
print(x)

name = 'shiva priya'
print(name.split())


#islower
x = name.islower()
y = name.isupper()
z = name.isalnum()
print(x)
print(y)
print(z)

print(len(name))

"""
append new string in the middle of a given string 

s1 = "Python"
s2 = "Luminar" 

o/p: PytLuminarhon

"""
s1 = "Python"
s2 = "Luminar"
mid = int(len(s1)/2)
x = s1[:mid]
x = x+s2
y = s1[mid:]
x = x+y
print(x)
"""
create a new string made of the first , 
middle, and last characters of each input string 

s1 = "Python"
s2 = "Luminar"

o/p: PLhinr
"""
s1 = "Python"
s2 = "Luminar"
first_char = s1[0]+s2[0]
# mid_char = s1[int(len(s1)/2) : int(len(s1)/2)+1]+s2[int(len(s2)/2):]

mid_chars1 = s1[int(len(s1)/2)]
mid_chars2 =  s2[int(len(s2)/2)]
print(mid_chars1)
print(mid_chars2)
mid_char = mid_chars1+mid_chars2
last_char = s1[-1]+s2[-1]
print(last_char)
char = first_char+mid_char+last_char
print(char)
