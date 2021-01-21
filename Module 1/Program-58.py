# 58.python program to demonstrate hirerchial inheritance
## c is derived from and  B is also derived from A ,two class derived from one class
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
obj1=A()
obj2=B()
obj3=C()
obj1.display1()
obj2.display2()
obj3.display3()
obj2.display1()
obj3.display1()
obj3.display2()##error becuase b class is not inherited

##output
'''class A Method
class B Method
class C Method
class A Method
class A Method
'''
