a= [ ]
row=int(input("Enter no. of elements in the row: "))
col=int(input("Enter no. of elements in the coloumn: "))
print("Enter elements of the first matrix : ")
for i in range(row):
    a.append([ ])
    for j in range(col):
        a[i].append(int(input()))
b=[ ]
print("Enter elements of the second matrix : ")
for i in range(row):
    b.append([ ])
    for j in range(col):
        b[i].append(int(input()))
c=[ ]
for i in range(row):
    c.append([ ])
    for j in range(col):
        c[i].append(a[i][j] + b[i][j])
for i in range(row):
    print(c[i])

        
