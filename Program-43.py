# 43.python script to find factorial of given number using recursive function
def factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
print(factorial(num)) 
