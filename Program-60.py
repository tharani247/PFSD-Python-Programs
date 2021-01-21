# 60.python program to demonstrate polymorphism(Method Overloading)
class shape:
    def area(s,a=None,b=None):
      if a!=None and b!=None:
        print("Area:",a*b)
      elif a!=None:##special literal None
          print("Area:",a*a)
      else:
          print("Area:",0)
          

s=shape()
s.area()
s.area(5)
s.area(4, 10)

'''output
Area: 0
Area: 25
Area: 40'''
