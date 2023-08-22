# file = open('sample.py','x')
# file = open('sample.txt','a')
# file.write(" To write to an existing file, you must add a parameter to the open() function:")
# file.close()
#
# file = open('sample.txt','r')
# print(file.read())

# file =  open('sample.txt','w')
# file.write('New line')
# #
# # with open('sample.txt','r') as file:
# #     print(file.read())
#
# # import os
# # # os.remove('sample.txt')
# #
# # file_path = r'test.txt'
# # # x = os.path.exists(file_path)
# # # if x:
# # #     print(f" {file_path} The file is existing")
# # # else:
# # #     print(f'the file {file_path} is not existing')
# # y = os.path.getsize('sample.txt')
# # print(y,'bytes')
#
# # with open(r'sample.txt','r') as file:
# #     lines = len(file.readlines())
# #     print('No. of lines:',lines)
#
#
# """"
# 6)  Delete Lines from a File in Python
# 7)	Writing List to a File in Python
# 8)	Python List Files in a Directory
# 9)	Python Count Number of Files in a Directory
# 10)	Python list Files in Directory with Extension txt
# 11)	Python Remove/Delete Non-Empty Folder
# 12)	Python Get File Creation and Modification DateTime
# """
#
#
# def delete_lines(file_path, lines_to_delete):
#     # Read the file content into a list
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#
#     # Identify the lines to delete
#     lines = [line for line in lines if line.strip() not in lines_to_delete]
#
#     # Write the updated content back to the file
#     with open(file_path, 'w') as file:
#         file.writelines(lines)
#
# file_path = 'sample.txt'
# lines_to_delete = ['2 a+ mode. The a+ mode in Python is used to open the','2 a+ mode. The a+ mode in Python is used to open the']
#
# delete_lines(file_path, lines_to_delete)
#
#
#
# # import fileinput
# #
# # def delete_lines(file_path, lines_to_delete):
# #     with fileinput.input(file_path, inplace=True) as file:
# #         for line in file:
# #             if file.lineno() not in lines_to_delete:
# #                 print(line.rstrip())
# #
# # # Example usage
# # file_path = 'sample.txt'
# # lines_to_delete = [2, 4]  # Line numbers to delete, starting from 1
# #
# # delete_lines(file_path, lines_to_delete)
#
# #
# # import os
# #
# #
# # def count_files(directory):
# #     count = 0
# #     for i, j, files in os.walk(directory):  # i for the current directory path  j represents the list of subdirectories
# #         print(files)
# #         count += len(files)
# #         print(count)
# #
# #     return count
# #
# #
# # # Example usage
# # directory_path = r'C:\Users\Luminar\PycharmProjects\May_Python\file_handling'
# # file_count = count_files(directory_path)
# # print(f"Number of files in the directory: {file_count}")
#
#
# # import os
# # #
# # def list_txt_files(directory):
# #     txt_files = [file for file in os.listdir(directory) if file.endswith(".txt")]
# #     return txt_files
# #
# # # Example usage
# # directory_path = r'C:\Users\Luminar\PycharmProjects\May_Python\file_handling'
# # txt_files = list_txt_files(directory_path)
# # for file in txt_files:
# #     print(file)
#
#
# listitems = ["Hi","How are you ","Welcome to python class"]
# with open("listitems.txt",'w')as file:
#      for i in listitems:
#         file.write(i+"\n")
#         # file.close()




file = open('sample.txt','r')
# file.seek(10)
# data = file.read()
# print(data)

line1 = file.readline()
print(line1)
position = file.tell()

print(position)
file.seek(10)
print(file.tell()) # current position of the file