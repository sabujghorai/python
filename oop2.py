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
