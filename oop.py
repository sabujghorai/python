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

# inheritence
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()

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
