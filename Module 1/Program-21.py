#21. Program to demonstrate pass statement
n=int(input("Enter Range"))
for i in range (n+1):
    if(i%2==0):
        pass
    else:
        print(i)
        
