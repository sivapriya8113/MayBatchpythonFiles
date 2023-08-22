"""
@static_method
---------------
allow you to group related functions together within a class.
even if those functions do not require access to instance-specific data.

"""

class Math:
    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def is_even(number):
        if number % 2 ==0:
            print("the num is even ")
        else:
            print("odd")
        # print("the num is even ")

result = Math.multiply(5, 3)
print(result)
(Math.is_even(10))
(Math.is_even(7))
