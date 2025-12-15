# first problem
meaning = {
  "table" : ["A peice of furiniture" , "list of facts and figure"],
  "cat" : "a small animal"
}
print(meaning)

# second problem
subject = {
  "python","java","c++","python","javascript","java","python","java","c++","c"
}
print(subject)
print("we need t total",len(subject),"classroom for study")

# third problem
# WAP toenter marks of 3 students from the user and store them in a dictionart. start with an empty dictionart & add one by one. use subject as key and marks as a value
marks = {}

a = int(input("enter the marks of physics :"))
marks.update({"physics" :a}) 

b = int(input("enter the marks of chemistry :"))
marks.update({"chemistry" :b})

c = int(input("enter the marks of maths :"))
marks.update({"maths" :c})

print(marks)
