a=[ ]
n=int(input("Enter number of elements in the list: "))
for i in range(n):
    a.append(int(input("Enter elements")))

print("Intermediate steps: ")
for i in range(0,n-1):
    min=a[i]
    pos=i
    for j in range(i+1,n):
        if(a[j]<min):
            min=a[j]
            pos=j
    temp=a[i]
    a[i]=a[pos]
    a[pos]=temp
    print(a)

