"""
1. WAP to check whether an element exist within a tuple
tuple1 = ("Apple", [10, 20, 30], (5, 12, 25),1,5,6,7)

2. to convert a tuple to a string
tuple2 = ("s","t","r","i","n","g")

3. count the number of occurance of item 50 from a tuple
tuple1 = (20,50,70,50,60,50)
"""
tuple1 = ("apple", [10, 20, 30], (5, 12, 25),1,5,6,7)
print("Apple" in tuple1)

tuple2 = ("s","t","r","i","n","g")
print(''.join(tuple2))


tuple1 = (20,50,70,50,50)
x = tuple1.count(20)
print(x)
#
#
#
#
# tuple1 = ("Apple", [10, 20, 30], (5, 12, 25),1,5,6,7)
# print("Apple" in tuple1)
#
#
# # # tuple1 = ("Apple", [10, 20, 30], (5, 12, 25),1,5,6,7)
# # # x = tuple1[1]
# # # print(x)
# # # print(x in tuple1)
# #
# tuple2 = ("s","t","r","i","n","g")
# x = "".join(tuple2)
# print(x)
# print(type(x))
#
# y = enumerate(tuple2)
# v = (list(y))
# print(v)
# print(type(v))
# #
# # """
# # zip
# # map
# # filter
# # reduce
# # """
# # print("priya " *4)
# #
tuple2 = (1,0)
x = all(tuple2)
print(x)
#syntax
#all(iterable)
# #
# # #any()
tuple2 = (1,0,9)
x = any(tuple2)
print(x)
# # y = ("apple","Orange","banana","aaaaaaaaa")
# # print(max(y))
# #
# #
# #
# tuples = (4,5,6,7,-5,True)
# print(all(tuples))
# print(any(tuples))