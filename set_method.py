roll = {"hello","world","sabuj"}
roll.add(1) # we can add one element by one parentheses
roll.add((2,3)) # we can add multiple elements by double parentheses
print(roll)

# remove method
roll.remove("hello") # removes the element 34
print(roll)
# pop method

print(roll.pop())
print(roll.pop())

# clear method
roll.clear()
print(roll)

set1 = {2,3,4,5}
set2 = {4,5,6,7}
print(set1.union(set2)) # combine both set valurs and return new (prints 2,3,4,5,6,7)
print(set1.intersection(set2)) # combine common values and return new (prints 4,5)
# set1.union(set2) = set2.union(set1)
