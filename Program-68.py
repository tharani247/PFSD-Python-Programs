#68.Python program to demonstrate multiple exception
try:
    l=[1,2,3,4,5]
    print(l[5])
    print(10/0)
except IndexError:
    print("Index Bound of exception")
except ZeroDivisionError:
    print("Divided by Zero exception")
else:
    print("No exception occured")
    

    
    
