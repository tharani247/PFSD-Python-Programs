# 45.python script to print sum of n  number using recursive function
def sum(n):  
   if n == 1:  
       return n  
   else:  
       return n+sum(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
print(sum(num)) 
