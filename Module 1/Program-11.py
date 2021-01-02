'''Python script to check whether citizen is eligible to voting or not'''
name=input('Enter Name')
a=int(input('Enter your Age'))
if(a>=18):
    print(name,"is eligible for voting")
else:
     print(name,"is not eligible for voting")
