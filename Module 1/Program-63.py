# 63.python program to demonstrate super() method
class Student:
    def __init__(s,id, name, age):
       s.id=id
       s.name=name
       s.age=age
class Faculty(Student):
    def __init__(s,id, name,age,status):
       super(). __init__(id,name,age)
       s.status=status
cse=Faculty(1,"Tharani",19,"single")
print(cse.id,cse.name,cse.age,cse.status)


'''output
1 Tharani 19 single'''
