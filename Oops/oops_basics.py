class Car():
    def __init__(self, car_name, model, color): # constructor
        self.car_name = car_name
        self.model = model
        self.color = color

    def drive(self):#method
        print("Driving",self.car_name,self.model)

    
obj = Car("Vento", 2023, "Grey")
print(obj.car_name)
print(obj.color)
obj.drive()



""""
Oops
----

1. class ----- It's collection of objs 
2. object  ---- instance of a class 
3. inheritance --- 
4. Polymorphism ---
5. Epcapsulation ---
6. Abstraction

"""