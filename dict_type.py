student = {
  "name" : "sabuj ghorai",
  "subject" : {
    "phy" : 87,
    "chem" : 89,
    "math" : 87
  }
}
print(student.values())
print(len(student)) # means total number of key value pairs...

# we can use typecasting inside the dictionary also 
print(list(student.keys()))

print(student.items()) # returns all (key , values ) pairs as tuple.. in parenthesis

print(student.get("subject")) # returns the key according to the value...

student.update({"eng" : 87}) # use to update inside the dict.. and the new dict should be in curly brckets
print(student )
