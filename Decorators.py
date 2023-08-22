"""
Decorators are allows you to modify the behaviour of a function or class without directly changing its source code.
decorators are functions that take another function or class as input and extend or modify its functionality.

@symbol
"""


#
# def deco_func(func):
#     def wrapper():
#         print("Before func execution")
#         func()
#         print("After function execution")
#     return wrapper()
#
#
# @deco_func
# def my_func():
#     print("Inside the my_func")
# # my_func()


def decor_func(func):
    def inner():  # inner func
        print("I got decorator")
        func()  # calling test_fun

    return inner  # return inner func


@decor_func
def test_fun():
    print("a test func")
test_fun()

# decorated_function = decor_func(test_fun)  # decorate the test_fun
# decorated_function()  # calling decorated func
