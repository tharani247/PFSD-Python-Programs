# 56.python program to demonstrate single inheritance
class A:
    def display1(a):
        print("class A Method")
class B(A):
    def display2(b):
        print("class B Method")
obj1=A()
obj2=B()
obj1.display1()
obj2.display2()
obj2.display1()

##output
'''class A Method
class B Method
class A Method
'''
