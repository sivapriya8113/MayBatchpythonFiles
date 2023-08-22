import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Tech@18oct", port=3306)

print(mydb)

mycursur = mydb.cursor()
# mycursur.execute("Create database maypython")
mycursur.execute("use maypython ")
# mycursur.execute("create table students(name varchar(250), age int, roll_num int)")
sql = "INSERT INTO students (name, age, roll_num) VALUES (%s, %s, %s)"
val = ("John",13, 21)
mycursur.execute(sql, val)
mydb.commit()

print(mycursur.rowcount, "record inserted.")
"""
Inner Join
----------

it combines rows from two or more tables based on specified 
condition and returns only the rows that have matching values in both tables.



select column1, column2,...
from table1
inner join table2 ON table1.column_name = table2.column_name ;

"""
