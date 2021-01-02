#30. Program to print prime numbers in the given range of a number 
import math
n=int(input("Enter yout number"))
flag=1;
k=math.sqrt(n)
l=int(math.ceil(k))
for i in range(2, n):
    if(n%i==0):
        flag=0
        print("not a prime number")
        break
    else:
        print(i)
