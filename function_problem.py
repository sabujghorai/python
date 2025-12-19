# average of 3 numbers
def average(a,b,c):
  avg = (a+b+c)/3
  print(avg)
  return sum

a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
c = int(input("Enter 3rd number :"))
average(a,b,c)

# default parameter
def sum(a=5,b=7):
  avg = (a+b)/2
  print(avg)
  return avg

sum() # we are not assigning the argument
