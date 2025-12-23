# print numbers in reverse order
b = int(input("Enter a number :"))

def show(n):
  if(n == 0): # base case
    return
  print(n)
  show(n-1) # function call

show(b)

# print the factorial of a number using recursion taking from user input

b = int(input("Enter a number :"))

def fact(a):
  if(a == 0):
    return 1
  return a*fact(a-1)

print("factorial of your given number is :",fact(b))

# print the sum of all n natural numbers

b = int(input("Enter a number :"))

def sum(a):
  if(a == 1):
    return 1
  return a+sum(a-1)

print("sum of your all natural number is :",sum(b))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the number of terms: "))

print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i), end=" ")

