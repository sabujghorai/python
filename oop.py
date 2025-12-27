class Car: # first letter must be capital letter 'c'ar
    car_name = "Mercedese Benz"
    model_no = 23
    colour = "Blue"

s1 = Car() # creating aa object
print(s1.car_name)
print(s1.model_no)
print(s1.colour)


# __init__ function --> also call constructor
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("mercedese","Benz")
print(my_car.brand)
print(my_car.model)
# making a new brand and model
my_new_car = Car("TATA","safari")
print(my_new_car.brand)
print(my_new_car.model)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Object creation
s1 = Student("Sabuj", 21)
s1.display()
