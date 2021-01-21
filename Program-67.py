#67.Python program to demonstrate exception handling-4
try:
    l=[1,2,3,4,5,6]
    print(l[7])
except IndexError:
    print("Index out of bounds error")
else:
    print("No exception occured")
    

    
    

