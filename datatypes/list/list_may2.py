"""
list
----
mutable(changable), indexed, ordered, allows duplicates


"""
list_items = ["apple","orange","mango","grapes"]
print(list_items)
print(list_items[0])
print(list_items[-1])
print(list_items[1:])
print(list_items[::-1])
print(list_items[:-1])
print(list_items[0][-2])
list_items[1]='pineapple'
print(list_items)
print(list_items[0][:1:-1])
# list_items[0][-2]='#'
# print(list_items)
list_items = ["apple","orange","mango","grapes",["python","react","django"]]

list_items[4].sort(reverse=True)
print(list_items)
# print(list_items[4][0])
# print(list_items[4][::-1])
# print(list_items[4][0][::-1])
# list_items[4].insert(1,'golang')
# print(list_items)
# list_items.append("angular")
# print(list_items)
#
# list2 = ["vento","bmw","audi","ford"]
# list_items[4].extend(list2)
# print(list_items)

# list_items[4].remove("python")
# print(list_items)

# list_items[4][:5].pop()
# print(list_items)
#
# list_items[4].clear()
# print(list_items)


# del list_items[4]
# print(list_items)


"""

"""