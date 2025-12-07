palindrom = []
palindrom.append(input("enter a number :"))
palindrom.append(input("enter a number :"))
palindrom.append(input("enter a number :"))
palindrom.append(input("enter a number :"))
palindrom.append(input("enter a number :"))

print("final list",palindrom)

temp = palindrom.copy()

if palindrom == temp():
    print("the number you have given is a palindrom element")
else:
  print("the number you have entered is not a palindrom number")
