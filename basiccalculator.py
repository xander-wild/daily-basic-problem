print("welcome to calculator \n")
a=int(input("enter first value"))
b=int(input("enter seconde value"))
print("which operation you want two perform \n add sub mul div")
c=input()
if c=="add":
    d=a+b
    print(d)
if c=="sub":
    d=a-b
    print(d)
if c=="mul":
    d=a*b
    print(d)
if c=="div":
    d=a/b
    print(d)
