"""
create , write, read, delete, add
x, w, r, remove , append



"""

# file = open('myfile.txt','w')
# file.write("Hi dears szxdfcvghbvbndc ")
# file.close()
#
# file = open("myfile.txt",'r')
# print(file.read())
# file.close()
#
# file = open('myfile.txt','a')
# file.write('Python django fullstack course')
# file.close()
# file = open("myfile.txt",'r')
# print(file.read())
# file.close()


with open('new.txt', 'r') as file:
    # print(file.read())
    print(len(file.readlines()))
    file.close()

#
# import os
#
# os.remove('myfile.txt')
