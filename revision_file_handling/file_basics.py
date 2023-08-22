"""
File handling : Write , Read , Create , delete , append
modes: w, r, x, remove, a , w+, r+ , a+

"""

""""
6)  Delete Lines from a File in Python
7)	Writing List to a File in Python
8)	Python List Files in a Directory
9)	Python Count Number of Files in a Directory
10)	Python list Files in Directory with Extension txt
11)	Python Remove/Delete Non-Empty Folder
12)	Python Get File Creation and Modification DateTime
"""
# 6)  Delete Lines from a File in Python

# with open("maybatch.txt",'w')as file:
#     file.write('Hi dears  welcome to file handling session sdfghjbvcfdrtyuhgftyguh ')
#     file.close()
#
# with open('maybatch.txt','r') as file:
#    x = file.readlines()
#    lines_to_delete = [2,4]
#    lines = [line for line in x if line.strip() not in lines_to_delete]
#    with open('maybatch.txt','w')as file:
#       file.writelines(lines)


# import  os
# file = 'maybatch.txt'
# os.remove(file)

# import fileinput
#
# file = 'maybatch.txt'
# lines_to_delete = [3,5]
#
# def delete_line(file, lines_to_delete):
#       with fileinput.input(file, inplace=True) as file:# fileinput.input is used to open the file in-place for modification
#                                                 #inplace = True changes are written back to the same file
#         for i in file:
#             if file.lineno() not in lines_to_delete:
#                # print(file.lineno() )
#               print(i.rstrip())
#
# delete_line(file,lines_to_delete)

# 8)	Python List Files in a Directory

#
directory_path = r'C:\Users\Luminar\PycharmProjects\May_Python\file_handling'
def list_files(directory_path):
    file = os.listdir(directory_path)
    return file

file_list = list_files(directory_path)
print((file_list))
for i in file_list:
    print(i)





import os

directory = r'C:\Users\Luminar\PycharmProjects\May_Python\file_handling'


# def count_files(directory):
#     count = 0
#     list_file = os.listdir(directory)
#     for i in list_file:
#         count=count+1
#     print(count,"num of files in this directory ")
# count_files(directory)

# 10)	Python list Files in Directory with Extension txt

def list_txt_files(directory):
    txt_files = [file for file in os.listdir(directory) if file.endswith("csv")]
    return txt_files


print(list_txt_files(directory))
