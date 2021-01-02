#25. Program to check whether the given number is prime number or not 
import math
n=int(input("Enter Range"))
flag=1;
k=math.sqrt(n)
l=int(math.ceil(k))
for i in range(2, l):
    if(n%i==0):
        flag=0
        break
if(flag==0):
    print("given number is not prime")
else:
    print("given number is prime")

    
        
        
