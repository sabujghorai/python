# del keyword
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("sabuj")
print(s1.name) # first it will print the name sabuj
del s1.name # output will be an error because name attribute is already deleted
print(s1.name)# error
