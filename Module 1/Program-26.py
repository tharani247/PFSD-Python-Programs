#26. Program to check whether the given number is armstrong number or not 
n=int(input("Enter yout number"))
flag=1
sum=0
l=n
print(l)
while(l>0):
    rem=l%10
    sum+=(rem**3)
    l //= 10
    print(l)
    
if(sum==n):
    print("given number is armstrong")
else:
    print("given number is not armstrong")

    
        
        
