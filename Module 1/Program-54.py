# 54.python program to demonstrate parameterized constructor
class Employee:
    def __init__(e,id,name):
        print("parameterized constructor")
        print("Employee id",id,"Employee name",name)
        
emp=Employee(19, "hello")#to create an object

