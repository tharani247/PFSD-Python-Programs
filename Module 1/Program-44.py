# 44.python script to find fibonnacii sequence upto  given number using recursive function
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
# take input from the user  
num = int(input("Enter a number: "))
print("Fibonacci sequence:")
for i in range(num):
       print(recur_fibo(i))

