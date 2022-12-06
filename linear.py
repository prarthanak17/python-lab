list1=[]
print("Enter the length of list")
l=int(input())
for i in range(l):
    N=int(input("Enter the list values"))
    list1.append(N)
print(list1)
def linear_search(list1,n,key):
    for i in range(0,n):
        if(list1[i]==key):
            return i
        else:
            return -1
n=l
key=int(input("Enter the value to be searched:"))
res=linear_search(list1,n,key)
if(res==-1):
    print("Element not found")
else:
    print("Element found at index:",res)
