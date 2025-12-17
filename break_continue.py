 # BREAK STATEMENT

i = 1
while i<=5:
  print(i)
  if i == 4:
     break
  i += 1

  print("loop terminate") # this print is inside the loop because tab is given at the first
print("loop turminate") # and this print is outside the loop

# CONTINUE STATEMENT
i = 1
while i <= 15:
   if i == 3: # 3 will not print 
      i += 1
      continue
   print(i)
   i+=1
