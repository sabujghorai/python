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
    __name = "hello" # creating a private class 

    def __hello(): # creating a private object
        print("hello world")

p1 = Person()
print(p1.__name)# it will also show an erroor because the __name ia a private attribute
