A=[ ]
print("Merge sort : ")
n=int(input("Enter number of elements: "))
for i in range(0,n):
    x=int(input("Enter elements %d : " %(i+1)))
    A.append(x)
print("Before sorting: ")
print(A)
def merge(left,right,A):
    i=j=k=0
    while(i<len(left) and j<len(right)):
        if (left[i]<right[j]):
            A[k]=left[i]
            i=i+1
        else:
            A[k]=right[j]
            j=j+1
        k=k+1
    while(i<len(left)):
        A[k]=left[i]
        i=i+1
        k=k+1
    while(j<len(right)):
        A[k]=right[j]
        j=j+1
        k=k+1
    print("Merging",A)
def Mergesort(A):
    print("Splitting",A)
    n=len(A)
    if( n>1):
        mid=n//2
        left=A[:mid]
        right=A[mid:]
        Mergesort(left)
        Mergesort(right)
        merge(left,right,A)
Mergesort(A)
print(A)

        
