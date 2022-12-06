
list1=[]
l=int(input("Enter the number of elements:"))
for i in range(l):
    n=int(input("Enter the elements of the list"))
    list1.append(n)
print(list1)
print("The largest element in the list is:",max(list1))
count={}
for i in range(l):
    count.setdefault(list1[i],0)
    count[list1[i]]+=1
print("The frequency of largest number is:")
print(count[max(list1)])
