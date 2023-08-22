"""
child class(derived class,sub class)  inherits the properties of parent class (super class, base class)


code reusability

Types of inheritance
---------------------

1. Single inheritance
2. Multiple
3. Hierarchical
4. Multilevel
5. Hybrid



"""


class Animal:  # parent class
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def test(self):
        print("parent class")


class Dog(Animal):  # child class
    def speak(self):
        print("dog name is ", self.name, self.category)


class Cat(Animal):  # child class
    def speak(self):
        print("Cat name is ", self.name, self.category)


obj_dog = Dog("Rocky", "Pet")
obj_dog.test()

obj_dog.speak()
# obj_cat = Cat("kitty","ASDFGHJ")
# obj_dog.speak()
# obj_cat.speak()
