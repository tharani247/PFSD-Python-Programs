#27. Program to check whether the given number is palindrome number or not 
n=int(input("Enter yout number"))
flag=1
sum=0
l=n
print(l)
while(l>0):
    rem=l%10
    sum= (sum*10)+(rem)
    l //= 10
print(sum)
if(sum==n):
    print("given number is palindrome")
else:
    print("given number is not palindrome")

    
        
        
