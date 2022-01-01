#Python Program to find sum of array
"""arr1 =[10,12,4,8]
arr=len(arr1)
sum1 = 0
for i in  range (arr) :
    sum1= sum1 + arr1[i]
print(sum1)"""
def largestno(arr,n):
    max = arr[0]
    for i in range (1,n):
        if arr[i]>max :
            max=arr[i]

    return max  

arr=[12,2,12,23,23]
n=len (arr)
ans=largestno(arr,n)
print("largest no is ",ans )