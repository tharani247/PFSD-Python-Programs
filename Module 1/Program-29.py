#27. Program to print factors of a given number
n=int(input("Enter yout number"))
for i in range(1, n+1):
    if(n%i==0):
        print(i)
