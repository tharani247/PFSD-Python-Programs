#20. Program to demonstrate continue statement
n=int(input("Enter Range"))
i=1
for i in range (n+1):
    if(i==5):
        continue
    else:
        print(i)
        i+=1
    

