"""
List
----
List items are ordered, changeable, and allow duplicate values and indexed.

"""
list_items = ["apple","orange","mango","grapes"]
print(list_items)

#indexing
print(list_items[2])
print(list_items[-1])
print(list_items[:-1])
print(list_items[1:])
print(list_items[0][-1])
list_items[1]="pineapple"
print(list_items)

str1 = "hi dears"

x = list(str1)
print(x)
x[1]="v"
print(x)
print("".join(x))
x = list_items[2].replace('mango','#')
print(x)
list_items = ["apple","orange","mango","grapes",['python','django','react','java']]
print(list_items[4][0])
print(list_items[4][0][0])
list_items[4][1]='Angular'
print(list_items)

list_items.append('vue.js')
print(list_items)
list_items[4].insert(1,'golang')
print(list_items)
list_items.remove("apple")
print(list_items)
list_items.pop(1)
print(list_items)
# list_items.clear()
# print(list_items)
# del list_items
# print(list_items)
#
# list_items.reverse()
# print(list_items)
list_items = ["apple","orange","mango","grapes",['python','django','react','java']]
x = ['python','django','react','java']
x.sort(reverse=True)
print(x)

