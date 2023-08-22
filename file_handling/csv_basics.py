import csv


# #
# with open('business.csv','r')as file:
#     x = csv.reader(file)
#     for i in x:
#         print(i)
#
# with open('test.csv','w')as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Hi'])
#     writer.writerow(['How are you'])
#     writer.writerow(['Python class'])
#
with open('test.csv','r',newline='\n')as file:
    reader = csv.DictReader(file)
    for i in reader:
        print(i)




with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
# with open('names.csv','r')as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)
# csvfile.close()

with open('test_data.csv', 'w') as csvfile:
    fieldnames = ["Firstnaame", "Lastname", "Age", "Year"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Firstnaame": "Nithin", "Lastname": "PM", "Age": 23, "Year": 1234})
    writer.writerow({"Firstnaame": "Albin", "Lastname": "cv", "Age": 23, "Year": 1234})
    csvfile.close()
#
# with open('test_data.csv', 'r') as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         print(row)
#
# # with open("sample_data.csv",'w')as file:
# #     writer = csv.writer(file)
# #     writer.writerow(["s.no","names","course","place"])
# #     writer.writerow(['1','priya','python','asdfg'])
# #     file.close()
# #
# # with open('sample_data.csv','r')as file:
# #     reader =csv.reader(file)
# #     for row in reader:
# #         print(row)
#
# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
