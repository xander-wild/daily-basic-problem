#Python Program to check Armstrong Number
#Difficulty Level : Medium
#Last Updated : 12 Aug, 2020
#Given a number x, determine whether the given number
#  is Armstrong number or not. A positive integer of n
#  digits is called an Armstrong number of order n
#  (order is number of digits) if.

#abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 

#153= pow(1,3)+pow(5,3)+pow(3,3)
i = int(input (" enter the number:"))
orig=i
sum=0
j=str(i)
j=len(j)
while (i>0) :
    sum =sum + (i%10)**j
    i=i//10

if orig==sum:
    print("  armstrong")
else :
    print(" not armstrong")
