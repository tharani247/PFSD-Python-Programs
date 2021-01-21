#64.Python program to demonstrate exception handling-1
try:
    a=int(input("enter first value "))
    b=int(input("enter second value "))
    print(a/b)
except ZeroDivisionError:
    print("Divided by Zero exception")
