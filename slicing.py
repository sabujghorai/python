a = "jawahar"
print(a[2:4]) # prints the 'wa'.. "the ending index does not takes the value"
print(a[2:len(a)]) # ---> 'wahar'
print(a[2:]) # [2:len(a)] ---> 'wahar
print(a[:4]) # [0 : 4] ---> 'jawa'

#. NEGETIVE INDEXING 
a = "sabuj"
print(a[1:-2]) # [1:(n-2)=3] ---> [1:3] ---> ab
