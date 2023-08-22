"""
Fuctions

1. difference b/w args and parameters
    A parameter is the variable listed inside the parentheses in the function definition.
    An argument is the value that is sent to the function when it is called.
2. Create a function
    def my_func():
    print(" Welcome to python class  ")
    my_func()

3. Arguments (*args)
4. Call a function
5. Arbitary arguments
6. Keyword Argumnets
   If a fuction have many arguments and we want to change the
   sequence of them then we have to use keyword args
7. Arbitary Keyword arguments (**kwargs)
8. Default values
"""


# Arguments  (args) / positional args
# def my_function(msg1,msg2):
#   print(msg1 + msg2)
# my_function(("How","are", "you"),("Python","Django","Hi dears","fghjk" ))
# my_function("how are you ","Hi dears")
#
# def sum(a,b):
#     sum = a+b
#     print(sum)
# sum(4,6)
# sum(4,6)
# sum(4,6)
# sum(4,6)
#
#
# #Arbitary arguments
# If the number of arguments is unknown, add a * before the parameter name:

def my_func(*names):
    print("Hi", names, "How r u ")


my_func('Jack', "priya", "ddxfcvgbhj", "sdrfghjkl")


# my_func("Jin")
# my_func("Jain")
# my_func("Shebi")
#
# #
# # #Keyword arguments
# def my_function(Name1, Name2, Name3):
#     print("last name is  " + Name2)
#
#
# my_function(Name3="Jin", Name2='jack', Name1='jerrin')
#
#
# # Arbitary Keyword arguments (**kwargs)
# def my_function(**employee):
#     print("name of the employee is " + employee["name"])
#
#
# my_function(name="shiva", dept="python", id=78, salary=4567890, )
#
#
# #
# #
# # #Default value
# def my_function(country="Norway"):
#     print("I am from " + country)
#
#
# my_function()
# my_function("Sweden")
# my_function("India")


def student(name,course,id):
    print("student details:" ,name,id,course)

student('priya',12,'python')