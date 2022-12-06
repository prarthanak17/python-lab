
num=[]
l=int(input("Enter the number of elements"))

for i in range(l):
    n=int(input("Enter the list elements"))
    num.append(n)
print("The original list is:")
print(num)
print("Numbers in ascending order is:")
num.sort()
print(num)
print("Numbers in descending order is:")
num.sort(reverse=True)
print(num)

