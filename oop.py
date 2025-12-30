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

# basic class and object
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

# Rectangle area (Method example)
class Rectangle:
    def set_values(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r = Rectangle()
r.set_values(5, 3)
print("Area:", r.area())


class Student:
    collage_name = "Brainware Univercity"
    name = "Mr."
    #default constructor
    def __init__(self):
        pass

    #parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("from :",Student.collage_name)


c1 = Student("karan","unknown")
print(c1.name) # print name karan first 
# because object preference > the class preference


# opp class with methods methods 
class Student:
    def __init__(self,fullname):
        self.name = fullname


    def welcome(self):
        print("welcome Students",":",self.name)

s1 = Student("sabuj")
s1.welcome()
