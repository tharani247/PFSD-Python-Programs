#70.Python program to demonstrate raise block

try:
    raise IndexError
except IndexError:
    print("Index Bound of exception")
except ZeroDivisionError:
    print("Divided by Zero exception")
else:
    print("No exception occured")
    

    
    


    

    
    


