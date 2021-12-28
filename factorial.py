#Python Program for factorial of a number
#Difficulty Level : Basic
#Last Updated : 09 Aug, 2021
#Factorial of a non-negative integer, is multiplication
# of all integers smaller than or equal to n.
#  For example factorial of 6 is 6*5*4*3*2*1 which is 720.

n=int(input("enter no for which you want to find factorial "))
if n<0:
    print(0)

elif n==0:
    print(0)            #if input is less than 0 or 0 then print 0 

else :
    fact = 1
    while(n > 1):       #this loop will perform its action until 
                        #n is greater than 1
        fact *= n
        n -= 1
    print(fact)

# Python 3 program to find
# factorial of given number
 
#def factorial(n):
 
    # single line to find factorial
  #  return 1 if (n==1 or n==0) else n * factorial(n - 1)
 
 
# Driver Code
#num = 5
#print ("Factorial of",num,"is",
#      factorial(num))
 
n=int(input("enter"))
fact=1
while( n > 1):
        fact *= n
        n -= 1
        print(fact)
