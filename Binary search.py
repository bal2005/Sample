a=[ ]
n=int(input("Enter no. of elements in the list : "))
for i in range(0,n):
    x=int(input("Enter elements : "))
    a.append(x)
e=int(input("Enter target element: "))
first=0
last=n-1
while(first<=last):
    mid=(first+last)//2
    if e>a[mid]:
        first=mid+1
    elif e<a[mid]:
        last=mid-1
    else:
        print("Element found at position",mid+1)
        break
else:
    print("Element not found ")
        
