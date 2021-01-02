'''Python script to display largest number among three numbers using nested if else'''
a=int(input('Enter first value'))
b=int(input('Enter Second value'))
c=int(input('Enter Third value'))
if(a>b and a>c):
    print(a, "is big")
elif(b>c):
    print(b, "is big")
else:
    print(c, "is big")
