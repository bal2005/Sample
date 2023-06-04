row=int(input("Enter no. of rowss in the first matrix:"))
col=int(input("Enter no. of coloumns in the first matrix:"))
row1=int(input("Enter no. of rows in the second matrix:"))
col1=int(input("Enter no. of coloumns in the second matrix:"))
if(col==row1):
    print("Enter elements for the first matrix: ")
    X=[[int(input()) for j in range(col)]for i in range(row)]
    print("Enter elements for the second matrix: ")
    Y=[[ int(input()) for i in range(col1)]for i in range(row1)]
    result=[[0 for j in range(col1)]for i in range(row)]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j]+= X[i][k] + Y[k][j]
for r in result:
    print(r)
    break
else:
    print("Multiplication not possible ")
