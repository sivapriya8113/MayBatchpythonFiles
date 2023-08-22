# file=r'myfile'
# x=os.path.exists(file)
# if x:
#     print(f'{file} the file is exists')
# else:
#     print(f'{file} the file is not exists')

# file_name="myfile"
# file=open('myfile','a')
# file.write('hi dears')
# file_size=os.stat(file_name)
# print(f'file size{file_size.st_size}')


# file = open('new.txt','w')
# file.write('hello....\n')
# # with open('new.txt')as file:
# #     print(file.read())
# #     file.close()


# file = open('new.txt','a')
# file.write('welcome')
# with open('new.txt')as file:
#     print(file.read())


# file = open('new.txt','r')
# print(len(file.readlines()))
# st=input("enter the string to search")
# with open("new.txt")as file:
#     x=file.read()
#     if st in x:
#         print("string found")
#     else:
#         print("string not found")

#
# import linecache
# specific_line = linecache.getline("new.txt",2)
# print(specific_line)

#
# with open('new.txt','r+') as file:
#     # file.read()
#     file.write('new line \n')
#     file.write('second line \n')
#     lines = file.read()
#     print(lines)
#     # file.close()

# #
# with open('new.txt','r') as file:
#     # file.seek(2)
#     lines = file.readlines()
#     x = lines[1]
#     lines.remove(x)
#     print(lines)
#     file.write()


"""
1.write a python program to find the longest words from a file.

2.

"""

# def longst_word(filename):
#     with open(filename,'r')as infile:
#         words = infile.read().split()
#         # print(words)
#     max_len = len(max(words,key=len))
#     # print((max_len))
#     return [word for word in words if len(word)==max_len]
# print(longst_word('new.txt'))

# with open('new.txt','r') as file:
#     lines = file.readlines()
#     ptr = 1
#     with open('new.txt','w') as fi:
#         for line in lines:
#             if ptr !=5:
#                 fi.write(line)
#             ptr += 1
# print("deleted")
