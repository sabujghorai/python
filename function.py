def sum(a,b): # def means define --> a and b is parameters
  sum = a+b 
  print("sum of your two number is :",sum) # function definition
  return sum

a = int(input("Enter a number :"))
b = int(input("Enter a another number :"))
sum(a,b) # function call --> a,b is arguments

# default parameter
def sum(a=5,b=7):
  avg = (a+b)/2
  print(avg)
  return avg

sum() # we are not assigning the argument

def greet(name):
    """Prints a personalized greeting message."""
    print(f"Hello, {name}!")

# Call the function
greet("John")

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(2, 3)
print(result)  # Output: 5
