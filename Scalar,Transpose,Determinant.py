X=[ [1,3,5],
        [2,4,8],
        [13,15,17] ]

scalar=trans=[ [0,0,0],
                        [0,0,0],
                        [0,0,0] ]

k=int(input("Enter scalar value to multiply: "))
for i in range(len(X)):
    for j in range(len(X)):
        scalar[i][j]= X[i][j]*k
for r in scalar:
    print(r)

for i in range(len(X)):
    for j in range(len(X)):
        trans[j][i]= X[i][j]
for r in trans:
    print(r)

a=X[0][0]
b=X[0][1]
c=X[0][2]
d=X[1][0]
e=X[1][1]
f=X[1][2]
g=X[2][0]
h=X[2][1]
i=X[2][2]

det=a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
print("Determinant =",det)
