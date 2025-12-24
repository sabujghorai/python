# syntax for reading a file
f = open("demo.txt","r") # first quotation = file name ,second quotation = mode
print(f.read(10)) # only prints the 10 character of the file
print(f.readline()) # read one line at a time
print(f.read()) # read entire file
print
f.close() # closing the file
