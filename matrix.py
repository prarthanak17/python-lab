r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of columns:"))
matrix1=[]
for i in range(r):
    l=[]
    for j in range(c):
        j=int(input("Enter the elements of First Matrix Number"))
        l.append(j)
    matrix1.append(l)
matrix2=[]
for i in range(r):
    m=[]
    for j in range(c):
        j=int(input("Enter the elements of second Matrix Number"))
        m.append(j)
    matrix2.append(m)
for i in range(r):
    for j in range(c):
        print(matrix2[i][j],end=" ")
    print()
print("1st matrix")
for i in range(r):
    for j in range(c):
         print(matrix1[i][j],end=" ")
    print()
print("2nd matrix")
for i in range(r):
    for j in range(c):
        print(matrix2[i][j],end=" ")
    print()
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(r):
    for j in range(c):
        result[i][j]=matrix1[i][j]+matrix2[i][j]


print("Result Matrix")
for i in range(r):
    for j in range(c):
        print(result[i][j])
