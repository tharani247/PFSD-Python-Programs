# 32.Python program to demonstrate to dictionary collection operations
d1={}
print(d1)
d1={1:'baby','age':19,'G':'F', 1:2002}
print(d1)
print(d1.keys())
print(d1.values())
print(len(d1))
print(d1.items())
print(d1[1])
print(d1.get('G'))
d2=d1.copy()
print(d2)
d2.clear
print(d2)
d1.setdefault('status')
print(d1)
d1['status']='single'
print(d1)
d1.update(dob='feb', dad='venkatesh')
print(d1)
d1.update([(1,5)])
print(d1)
print(d1.pop(1))
print(d1)
del d1['G']
print(d1)
str(d1)
