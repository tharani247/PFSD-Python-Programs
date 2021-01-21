# 34.Python program to demonstrate to set collection operations

t={1,2,3,4,5}
u={1,2,3,4,5,6}
print(t)
print("length = ", len(t))
t1 =str(t)
print(t1)
print("Type = ", type(t))
print("sorted = ", sorted(t))
t2=tuple(t)
print(t2)
t3=list(t)
print(t3)


print(t.intersection(u))
print(t.intersection_update(u))
print(t.difference(u))
print(t.difference_update(u))
t.add(8)
print(u.remove(6))
print(t.pop())
print(u.symmetric_difference(t))
print("sum = ", sum(t))
print("max = ", max(u))
print("min = ", min(u))






