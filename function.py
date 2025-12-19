def sum(a,b): # def means define --> a and b is parameters
  sum = a+b 
  print("sum of your two number is :",sum) # function definition
  return sum

a = int(input("Enter a number :"))
b = int(input("Enter a another number :"))
sum(a,b) # function call --> a,b is arguments
