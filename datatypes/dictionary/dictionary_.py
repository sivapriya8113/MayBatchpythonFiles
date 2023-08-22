"""
Dictionary
---------

mutable, ordered,indexed, duplicates  not allowed

"""
dict1 = {"name":"priya","age":12,"place":'abc',"course":"python"}
print(dict1)

print(dict1["age"])
print(dict1.get("name"))
dict1["name"]="sreejith"
print(dict1)
dict1.update({"qulaification":"Btech","Role":"training"})
print(dict1)
print(dict1.keys())
print(dict1.values())

dict_keys=(['name', 'age', 'place', 'course', 'qulaification', 'Role'])
dict_values=(['sreejith', 12, 'abc', 'python', 'Btech', 'training'])

print(dict(zip(dict_keys,dict_values)))

dict1 = {"name":"priya","age":12,"place":'abc',"course":"python"}
# dict1.pop("name")
print(dict1)
dict1.popitem()
print(dict1)


#
# x = {"name":"adwaith","age":12,"course":"python"}
#
# print(dict1["name"])
# print(dict1.get("name"))
# dict1["name"]="Aiswarya"
# print(dict1)
# dict1.update({"course":"React"})
# print(dict1)
# dict1.update({"Qualification":"BTech","Role":"training"})
# print(dict1)
# x = dict1.keys()
# print(x)
# y = dict1.values()
# print(y)
# # dict1.pop("name")
# # print(dict1)
# dict1.popitem()
# print(dict1)
