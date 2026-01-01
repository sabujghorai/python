# del keyword
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("sabuj")
print(s1.name) # first it will print the name sabuj
del s1.name # output will be an error because name attribute is already deleted
print(s1.name)# error

# Private(like) attribute & method
class Account:
    def __init__(self,acc_num,acc_pass):
        self.acc_num = acc_num # public attribute
        self.__acc_pass = acc_pass # private attribute 

     def reset_pass(self):
        print(self.__acc_pass)

a = Account("123456","pass@1234")
print(a.acc_num)
print(a.reset_pass()) # now it will orint the password
print(a.__acc_pass)# print error 'Account' object has no attribute 'acc_pass'
class Person:
    __name = "hello" # private class attribute

    def __hello(self): # creating a private object
        print("hello users")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())
# print(p1.__name)# it will also show an erroor because the __name ia a private attribute

# Inheritence
class Car:
    colour = "black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car): # the Toytacar is the subcatagory of the Car
    def __init__(self,name):
        self.name = name

c = ToyotaCar("toyota corola")
print(c.name)
print(c.colour)
print(c.start())

# Question
#create an ElectricCar class that inherits the car class and has an additional attribute battery_size
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class ElectricCar(Car): # The Car inheritence added
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85KWh")
print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.battery_size)
# these are the single lever inheritence

# multi level inheritence
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __ini__(self,name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("Electric car..")
car1.start()
print(car1.type)
