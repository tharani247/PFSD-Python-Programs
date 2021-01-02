'''Python script to display largest number among three numbers using nested if else'''
a=int(input('Enter first value'))
b=int(input('Enter Second value'))
c=int(input('Enter Third value'))
if a>b:
    if a>c:
        print("a is big")
    else:
        print("c is big")
else:
    if b>c:
        print("b is big")
    else:
        print("c is big")
