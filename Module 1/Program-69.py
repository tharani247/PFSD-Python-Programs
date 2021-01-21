#69.Python program to demonstrate finally block
try:
    l=[1,2,3,4,5]
    print(l[5])
except IndexError:
    print("Index Bound of exception")
finally:
    print("End of program")
    

    
    

