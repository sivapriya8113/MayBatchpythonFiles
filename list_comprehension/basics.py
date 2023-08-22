list_items = [1,8,3,4,5,6,7]
even = []
odd =[]
for i in list_items:
    if i %2 ==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

even = [i*2 for i in list_items if i%2==0]
print("even nums",even)
odd = [j for j in list_items if j%2 !=0]
print(odd)





list_items = [1,8,3,4,5,6,7]
# newlist = [(i,'even' if i%2==0 else 'odd') for i in list_items]
# print(newlist)
# for key , value in enumerate(obj):
#     print("{} is {} number".format(key,value))
"""
#syntax
#newlist = [expression for item in iterable if condition == true]

list comprehension offers a shorter syntax when you want
 to create a new list based on the values of an existing list 
"""
fruits = ['apple', 'orange', 'banana', 'kiwi', 'grapes']
# newlist = []
# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)
# print(newlist)
#
# fruits = ['apple', 'orange', 'banana', 'kiwi', 'grapes']
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# list_items = [1, 8, 3, 4, 5, 6, 7]
# even = [i for i in list_items if i % 2 == 0]
# print(even)
# odd = [i for i in list_items if i % 2 != 0]
# print(odd)

# list_items = [1, 8, 3, 4, 5, 6, 7]
# prime_num = [x for x in list_items if all(x%y != 0  for y in range(2,x)) and x>1]
# print(prime_num)
#
# #list of numbers  is divisible by 3
#
#
# list1 = [i for i in range(100) if i%5==0 and i%2==0]
# print(list1)
#
# for i in range(1,51):
#     if i % 3 == 0 :
#         print(i)
# fact = 1
# list1  = [fact*i for i in range(1,5)]
# print()

matrix = [[j for j in range(3)] for i in range(4)  ]
print(matrix)