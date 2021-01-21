#46.Python script to read n elements ,add them into list and find sum
num =int(input("Enter how numbers you want to add as list"))
list1=[]
for i in range(num):
    i=int(input("Enter Number "))
    list1.append(i)
print(sum(list1))
