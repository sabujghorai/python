# syntax for reading a file
f = open("demo.txt","r") # first quotation = file name ,second quotation = mode
print(f.read(10)) # only prints the 10 character of the file
print(f.readline()) # read one line at a time
print(f.read()) # read entire file
print
f.close() # closing the file

# 'r' --> open for reading (default)
# 'w' --> open for writing, truncating the file first
# 'x' --> create a new file and open for writing
# 'a' --> open for writing, appending to the end of  the file if it exist 
# 'b' --> binary Mode 
# 't' --> text mode (default)
# '+' --> open a disk file for updating(reading and writing)
f = open("demo.txt","w")
print(f.write("hello this is a new line")) # overwrite a the entire file
f.close()

f = open("demo.txt","a") # print the char at the end in the demo.txt file
print(f.write("\n i want to learn java script"))
f.close()

# if we don't have ant text file and we want to create it
# we can create it by using the write and append mode
f = open("sample.txt","w") # by default it will create a new file --> write mode
f.close()

#--> append mode
f = open("sample2.txt","a")
f.close()

f = open("demo.txt","r+") # no truncate means file delete nahi hota hay
print(f.write("abc")) # over write the file at the starting
# means if we write in a file something like this --> This is a sample file
# after using the r+ mode it will print " abcs uis a new file " here in "this" the thi has erased
# and insted of thi abc is added 
print(f.read())# reading the file after over writing 
f.close()

# append + mode "a+"
s = open("demo.txt","a+") # no truncate means file delete nahi hota hay
print(s.write("hello how are you all"))# it will edit the file at the end
# it will not overwrite the file
# means if we write in a file something like this --> This is a sample file
# it will edit the file at the end something like this --> This is a sample filehello how are you all
print(s.read())
s.close()

# write + mode
d = open("demo.txt","w+") # truncating means it will delete the whole file and newly write the good morning
print(d.write("good morning"))
d.close()

#  WITH SYNTAX --> it's a better syntax for openning or closing a file
with open("demo.txt","a+")as f: #--> the f is the variable we can assigning any thing else
    # and the "as" --> is the alias(উপনাম) of "f"
    data = f.write("good evening")
# insted of writing the upper syntax we can symply write a with syntax and we can edit or read or apped the file also
# this with syntax automatically closes the file

# deleting a file using python
import os
os.remove("demo.txt")

