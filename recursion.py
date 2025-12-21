# print numbers in reverse order
b = int(input("Enter a number :"))

def show(n):
  if(n == 0): # base case
    return
  print(n)
  show(n-1) # function call

show(b)
