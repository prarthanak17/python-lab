list1=[]
print("Enter the length of list")
l=int(input())
for i in range(l):
    N=int(input("Enter the list values"))
    list1.append(N)
print(list1)
def binary_search(list1,x):
    low=0
    high=l-1
    mid=0
    while low<=high:
        mid=(high +low)//2
        if list1[mid]<x:
            low=mid+1
        elif list1[mid]>x:
            high=mid-1
        else:
            return mid
    return -1

x=int(input("Enter the element to be searched"))
result=binary_search(list1,x)
if result!=-1:
    print("Element is present at index",str(result))
else:
    print("Element is not found in the list")
