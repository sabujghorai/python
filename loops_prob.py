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
