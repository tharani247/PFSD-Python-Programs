#28. Program to print divisors of a given number
n=int(input("Enter yout number"))
for i in range(1, n):
    if(n%i==0):
        print(i)
