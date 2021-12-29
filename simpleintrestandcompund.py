#Python Program for simple interest
#Difficulty Level : Easy
#Last Updated : 18 Apr, 2020
#Simple interest formula is given by:
#Simple Interest = (P x T x R)/100
#Where,
#P is the principle amount
#T is the time and
#R is the rate
import time
print("welcome to intrest calculator")
p=int(input("enter the deposit amont : "))
t=int(input("enter the time (years): "))
r=int(input("enter the rate of intrest:"))
si = int((p*t*r)/100)
print("your intrest will be : ")
time.sleep(2)
print(si)
time.sleep(3)
print(p+si," will be final amount  if your taking simpple intrest after ",t ,"year")
#Formula to calculate compound interest annually is given by: 
#A = P(1 + R/100) t 
#Compound Interest = A – P 
#Where, 
#A is amount 
#P is principle amount 
#R is the rate and 
#T is the time span
a = int(p*((1+r/100)**t))
time.sleep(1)
print("your compund intrest will be ")
time.sleep(2)
print(a-p)
time.sleep(3)
print(a ,"will be final amount if your taking compund intrest in ",t,"year")