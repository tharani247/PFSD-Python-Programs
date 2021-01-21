# 52.python program to demonstrate class and object using __init method
class Employee:
    def __init__(e, id, name):
        e.id=id
        e.name=name
    def display(e):
        print(e.id,e.name)
emp=Employee(101, "KLU")#to create an object
emp.display()
