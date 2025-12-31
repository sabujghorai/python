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

a = Account("123456","pass@1234")
print(a.acc_num)
print(a.__acc_pass)# print error 'Account' object has no attribute 'acc_pass'
