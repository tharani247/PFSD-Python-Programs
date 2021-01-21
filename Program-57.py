# 57.python program to demonstrate multiple inheritance
## c is derived from both B and A ,one class derived from two classes
class A:
    def display1(a):
        print("class A Method")
class B(A):
    def display2(b):
        print("class B Method")
class C(B, A):
    def display3(c):
        print("class C Method")
obj1=A()
obj2=B()
obj3=C()
obj1.display1()
obj2.display2()
obj3.display3()
obj3.display2()
obj3.display1()
obj2.display1()
obj3.display2()

##output
'''class A Method
class B Method
class C Method
class B Method
class A Method
class A Method
class B Method'''
