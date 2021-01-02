# Python program to print even natural numbers using for loop
n =int(input("Enter Range"))
for i in range(1,n+1):
    if i%2==0:
        print(i)
#u can also use x=range(n+1), for i in x:
