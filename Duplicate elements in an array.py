def dups(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                print(arr[j])

arr=(2,2,1,5,3,3,8,1)
print("Duplicate elements present in the array: ")
dups(arr)
            
