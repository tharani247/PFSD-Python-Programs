# 33.Python program to demonstrate to tuple collection operations
t=(1,2,3,4,5)
print(t)
print("length = ", len(t))
t1 =str(t)
print(t1)
print("Type = ", type(t))
print("count = ", t.count(5))
print("index = ", t.index(4))
print("sorted = ", sorted(t))
t2=set(t)
print(t2)
t3=list(t)
print(t3)
print(t[1:4])
print("sum = ", sum(t))
print("max = ", max(t))
print("min = ", min(t))





