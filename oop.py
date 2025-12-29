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

# class with methids
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))

# Encapsulation (Using Private Variable)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount(5000)
account.deposit(2000)
account.show_balance()
# Polymorphism
class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

b1 = Bird()
b2 = Penguin()

b1.fly()
b2.fly()

# Real-Life Example (Combined OOP)
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "vehicle started")


class Car(Vehicle):
    def start(self):
        print(self.brand, "car started with key")


car = Car("Toyota")
car.start()

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

# Inheritance Example
class Person:
    def display(self):
        print("I am a person")


class Teacher(Person):
    def teach(self):
        print("I teach students")


t = Teacher()
t.display()
t.teach()

# Encapsulation (Private Variable)

class User:
    def __init__(self, password):
        self.__password = password

    def show_password(self):
        print("Password:", self.__password)


u = User("abc123")
u.show_password()

# Polymorphism (Same Method Name)

class Shape:
    def draw(self):
        print("Drawing a shape")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class Square(Shape):
    def draw(self):
        print("Drawing a square")


shapes = [Circle(), Square()]

for s in shapes:
    s.draw()

# name and marks of a student
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
