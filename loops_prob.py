# this is the code for multiplication table of any number
a = int(input("Enter a number :"))

i = 1
while i<=10:
  print(i*a)
  i += 1
# this is the code for squre of numbers from one to n which is given by the user
n = int(input("Enter a number :"))
i = 1
while i<=n:
  print(i*i)
  i += 1
# this is the multiplication table using while loop
a = int(input("Enter a number :")) 

i = 1
while i<=10:
  print(i*a)
  i += 1

# print the elements of the following list using a for loop
[ 1,4,9,16,25,36,49,64,81,100]

list = [1,4,9,16,25,36,49,64,81,100]
for i in list:
  if i == 16:
    print("stop here")
    break
  print(i)
else:
  print("happy journy")

# print number from 1 to 100 using for loop & range function

for i in range(1,101):
  print(i)

  # print number from 100 to 1 using for loop and range function
for i in range(100,0,-1):
  print(i)

# print the multiplication table of a number n using for loop and range function

n = int(input("Enter a number :"))
for i in range(1,11):
  print(i*n)

# WAP to find the sun of first n numbers using while loop

n = int(input("Enter a number :"))
i = 1
while i<=n:
  print(i+1)
  i+=1


# WAP to find the sun of first n natural numbers using while loop
n = int(input("Enter a number:"))
sum = 0
for i in range(n+1):
  sum = sum+i
print("the sum is:",sum)
