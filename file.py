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
