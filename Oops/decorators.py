"""
@class_method
-------------

class methods used to create alternative ways of creating instances of a class.

"""


# class Myclass:
#     class_variable = "Hello world"
#
#     @classmethod
#     def class_method(cls):
#         print(cls.class_variable)
#
#
# Myclass.class_method()

#
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2*(self.length + self.width)
#
#     @classmethod
#     def create_square(cls,side):
#         return cls(side,side*side)
#
#
# rectangle = Rectangle(7,6)
# print(rectangle.area())
# print(rectangle.perimeter())
#
# square = Rectangle.create_square(4)
# print(square.area())
# print(square.perimeter())

class Bankaccount:
    interest_rate = 0.08

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds..!")

    @staticmethod
    def calculate_interest(self):
        return self.balance * self.interest_rate

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate
        print("classmethod, interest updated")


bank = Bankaccount("SBI7778", 10000)
print(Bankaccount.interest_rate)
Bankaccount.set_interest_rate(0.07)
print(Bankaccount.interest_rate)
interest = bank.calculate_interest()
print(interest)
