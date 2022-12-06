num=[]
l=int(input("Enter the number of elements"))
for i in range(l):
    n=int(input("Enter the list elements:"))
    num.append(n)
print("The original list is:")
print(num)
print("The number to be removed:")
p=int(input())
num.remove(p)
print(num)
