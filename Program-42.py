# 42.python script to demonstrate length arguments
def add(*a):
    total=0
    for n in a:
        total=total+n
    print(total)
    print(a)##print as tuple
add(3,6,7,8,9,2,4)





