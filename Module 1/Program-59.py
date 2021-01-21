# 59.python program to demonstrate hybrid inheritance
##combination of mmultiple and multilevel inheritance programs
class A:
    def display1(a):
        print("class A Method")
class B(A):
    def display2(b):
        print("class B Method")
class C(A):
    def display3(c):
        print("class C Method")
class D(B, A):##if we use A,B it shows methd resolution order
    def display4(d):
        print("class D Method")
obj1=A()
obj2=B()
obj3=C()
obj4=D()
obj1.display1()
obj2.display2()
obj3.display3()
obj4.display4()
obj2.display1()

obj3.display1()
obj4.display1()
obj4.display2()

##output

