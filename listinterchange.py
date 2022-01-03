#Python program to interchange first and last elements
#  in a listPython program to interchange first and 
# last elements in a list
def interchange(ls):
    size = len(ls)
    temp = 0 
    temp = ls [0]
    ls[0]=ls[size-1]
    ls[size-1]=temp 
    return ls
#Python program to swap two elements in a list
def swapspecific(ls):
    pos1=int(input("enter element postion 1 you want to swap"))
    pos2=int(input("enter element postion 2 you want to swap"))
    temp=0
    size=len(ls)
    if pos1 < size and pos2<size:
        temp = ls [pos1]
        ls[pos1]=ls[pos2]
        ls[pos2]=temp

        return ls
    else:
        print("position is out of bound ") 

# driver code 
ls = list(input())
print("orignal list :",ls)
a=interchange(ls)
print("interchnage of first and last element :",a )
print(swapspecific(ls))