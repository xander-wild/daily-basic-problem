a=int(input("enter first no "))
b=int(input("enter second no "))

if a>b:        ##there is also a simple way just by using maximum function
    print( a,"  is greater than ",b)

else :
    print(b, "is greater than ",a)

""" Python program to find the
# maximum of two numbers
 
 
def maximum(a, b):
     
    if a >= b:
        return a
    else:
        return b
     
# Driver code
a = 2
b = 4
print(maximum(a, b)) """

#diffrent method 
"""# Python program to find the
# maximum of two numbers
     
# Driver code
a = 2
b = 4
 
# Use of ternary operator
print(a if a >= b else b)"""