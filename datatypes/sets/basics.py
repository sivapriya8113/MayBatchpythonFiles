"""
set
---

1. unchangable , unordered , unindexed, duplicates not allowed
"""
# set1 = {"Safna",12,"python","BCA",12,"python"}
# print(set1)
#
# x = list(set1)
# print(x)
# print(x[0])
# #
# set1 = {"Safna",12,"python","BCA",12,"python",(1,2,3),set["fghj",78,'fghj']}
# print(set1)
# # x  = {set[789,98,87,9]}
# # print(type(x))
#
# set1 = set()
# print(type(set1))
# #
#
A = {"priya",12,"python","btech"}
B = {"Safna",12,"python","BCA","python"}

# print(A.union(B))
# print(A.difference(B))
# # print(A.difference(B))
# print(A.intersection(B))
A.difference_update(B)
print(A)
# A.intersection_update(B)
# print(A)