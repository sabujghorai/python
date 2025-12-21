# print numbers in reverse order
b = int(input("Enter a number :"))

def show(n):
  if(n == 0): # base case
    return
  print(n)
  show(n-1) # function call

show(b)

# print the factorial of a number using recursion taking from user input
# print the factorial of a number taking user input

b = int(input("Enter a number :"))

def fact(a):
  if(a == 0):
    return 1
  return a*fact(a-1)

print("factorial of your given number is :",fact(b))
