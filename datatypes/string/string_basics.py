str1 = "Hello world"
#string indexing
print(str1[0])
print(str1[4])
print(str1[8])
print(str1[-1])

#string slicing
print(str1[:6])
print(str1[1:5])
print(str1[:-2])
print(str1[:5:-1])
print(str1[::-1])
print(str1[5::-1])
print(str1[5:])
str1 = "Hello world"
print(str1[::-2])
print(str1[::])

#string methods
str1 = "Helloworld"
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.islower())
print(str1.isalnum())

list1 = ["applw","banana","orange"]
x = ' '.join(list1)
print(x)

name = "Priya shiva"
print(name.split())


name = "shivapriya"
print(name[3])
print(name[:-1])
print(name[:])
print(name[::])
print(name[:4:-1])
print(name[5:-1])
print(name[:])
# print(name[5:])
print(name[::-1])
print(name[::4])
