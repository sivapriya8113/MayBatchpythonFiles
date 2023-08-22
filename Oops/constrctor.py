#parametrized con

# class Myclass:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
# obj = Myclass("priya",12)

#default const
# class Myclass:
#     name = "priya"
#     def __init__(self):
#
#         pass
#
# obj = Myclass() # creating an object without passing parameters

class Myclass:
    def __init__(self):
        self.name  = "Priya"
        self.age = 12

obj = Myclass()
print(obj.name)