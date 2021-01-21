# 61.python program to demonstrate (Method Overriding)-same method in both classes
class A:
    def display(a):
        print("Class A Method")
class B(A):
    def display(b):
        print("Class B Method")
            

obj1=A()
obj2=B()
obj1.display()
obj2.display()
'''output
Class A Method
Class B Method'''
