"""

1.	Sum all the items in a list
         My_list = [1,2,3,4,5]


"""
# print("sum")
# My_list = [1, 2, 3, 4, 5]
# sum = 0
# for i in My_list:
#     sum = sum + i
# print(sum)
#
# #product
# print("product")
# pdt = 1
# for i in My_list:
#     pdt *=i
#     print(pdt)

"""
3.	Write a Python program to convert a list of characters into a string
s = ['p', 'y', 't', 'h',’o’,’n’]

"""

# s = ['p', 'y', 't', 'h','o','n',"9",'0']
# str1 = "" #empty string
# for i in s:
#     str1 += i
#     print(str1)

#
# name = "priya"
# x = name[1:]
# print(x)
# for i in x:
#     print(i)
#
# for i in "aswin":
#     print(i)

"""
for value in sequence:
    statement
    """

"""
 Write a program to separate negative and positive numbers 
 from a given list ?(accept input from the user.)
 
 numbers = [1,5,6,-5,-2,-1,-7]
"""
# numbers = [1, 5, 6, -5, -2, -1, -7,0]
# x = []
# y = []
# z = []
# for i in numbers:
#     if i>0:
#         x.append(i)
#     elif i ==0:
#         z.append(i)
#         print(z)
#     else:
#         y.append(i)
# print("Negative nums",y)
# print("Positive nums",x)

"""
3.	 Write a python program to find largest number in a given list without using max()
"""
mylist = [5,9,8,7,3,2]
max = mylist[0] #5
for i in mylist:
    if max<=i:
        max = i
print(max)

"""
["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
Write a python program to print website suffixes (com , org , net ,in) from this list.


"""
str1 = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
# str2 = []
# for i in str1:
#     if i not in str2:
#          s = i.split(".")[-1]
#             str2.append(i)
#     print(str2)

"""Write a python program to find the common numbers from two lists"""
list1 = [1,6,8,7,5]
list2 = [1,8,6,4,3,1]
new_list = []
new = []
for i in list1:
    for j in list2:
        # print(i,j)
      if i == j and i  not in new_list:
         new_list.append(i)

      # else:
      #     new.append(
print(new_list)
print(new)

#even
list1 = [1,6,8,7,5]
even = []
odd = []
for i in list1:
    if i %2==0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
"""
 Write a python program to remove repeated elements from a given list without using built-in methods
list_to_remove = ["let's","google","the","pineapple","photo","google","photo",""]

"""
list_to_remove = ["let's","google","the","pineapple","photo","google","photo",""]
final_list = []
for i in list_to_remove:
    if i not in final_list:
        final_list.append(i)
print(final_list)

"""

["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
Write a python program to print website suffixes (com , org , net ,in) from this list.

"""
Links = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]

for i in Links:
    print(i)
    suffix = i.split('.')
    print(suffix)
    print(suffix[-1])