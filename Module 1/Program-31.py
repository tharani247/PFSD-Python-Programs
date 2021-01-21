# 31.Python program to demonstrate to list collection operations

l=[10, 20, 30]
print(l[0],l[1], l[2])
l1=[40,50,60]
l.append(l1)
print(l)
l.insert(6, [1,2])
print(l)
l1=l+l1
print(l1)
l2=[1,2,3]
l2=l2*3
print(l2)
l.extend(l1)
print(l)
l.pop()
print(l)
l.remove(20)
print(l)
l.count(60)
print(l1)
l.extend([30, 40])
print(l)
l2.sort()
print(l2)
l2.reverse()
print(l2)
l.clear()
print(l2)
print(sum(l2))
print(min(l2))
l3=[4,5]
print(max(l3))
print(len(l3))
l4=l1.copy()
print(l4)
##slice operator -(start sto & step)
l1[::]
print(l1)
##l[:] or l1[::] - will print the entire list
l1[2:4]
print(l1)
##It will print only the 2,3 indexed elements it will skip the last element
l1[0:3:1]
print(l1)
## starts at0 and ends in between 2
del l1[2]
print(l1)

