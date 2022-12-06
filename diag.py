
r=int(input("Enetr the number of rows:"))
c=int(input("Enter the number of columns:"))
matrix=[]
for i in range(r):
    d=[]
    for j in range(c):
        j=int(input("Enter the first element of the matrix ["+str(i)+"] ["+str(j)+"] "))
        d.append(j)
    matrix.append(d)
print("Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
sum=0
for i in range(r):
    for j in range(c):
        if i==j:
            sum=sum+matrix[i][j]
print("The sum of diagonal elements is:")
print(sum)
