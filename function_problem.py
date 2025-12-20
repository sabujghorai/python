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

# sum of two numbers taking input from users
def number(a,b):
  sum = a+b
  print(sum)
  return

a = int(input("Enter a number:"))
b = int(input("Enter another number :"))
number(a,b)

# this is the code for finding factorial

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

# Take user input
try:
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is: {factorial(num)}")
except ValueError:
    print("Please enter a valid integer.")

# code for finding fibonacci series

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

n = 10  # Number of terms
print(f"Fibonacci Series up to {n} terms: {fibonacci(n)}")
