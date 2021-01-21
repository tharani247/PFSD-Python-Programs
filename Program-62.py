# 61.python program to count th number of instances created
class Student:
    count=0
    def __init__(s, name, age):
       s.name=name
       s.age=age
       Student.count= Student.count+1
    def display(s):
        print("Name:",s.name, "Age:",s.age)
obj1=Student("klu", 80)
obj2=Student("klu2", 81)
obj3=Student("klu3", 82)
obj1.display()
obj2.display()
obj3.display()
print("No of instances", Student.count)
'''output
Class A Method
Class B Method'''
