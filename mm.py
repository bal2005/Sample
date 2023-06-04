row=int(input("Enter No of Rows for 1st Matrix:"))
column=int(input("Enter No of column for 1nd Matrix:"))
row1=int(input("Enter No of Rows for 2nd Matrix:"))
column1=int(input("Enter No of column for 2nd Matrix:"))
if(column==row1):
    print('Enter the First Matrix Element One by One :')
    X = [[int(input())for j in range(column)] for i in range(row)]
    print('Enter the Second Matrix Element One by One :')
    Y = [[int(input()) for j in range(column1)] for i in range(row1)]
    result = [[0 for j in range(column1)] for i in range(row)]
    print("1st Matrix X:",X)
    print("2nd Matrix Y:",Y)
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for r in result:
    print(r)
else:
    print("Multiplication is not possible")
