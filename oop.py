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
    collage_name = "Brainware University"
    location = "Berasat"
    
    def __init__(self,fullname):
        self.fullname = fullname
        
    def hello(self): # method name is hello
        print(self.fullname)
        
s = Student("hello sabuj ghorai") #object name is 's'
s.hello() # to use method use write object name dot method name

# Question
# create student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("hi",self.name,"your avg score is",sum/3)

s = Student("Krishna", [95,97,99])
print(s.name,s.marks)
s.average()
