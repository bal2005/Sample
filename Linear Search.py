alist=[]
n=int(input("Enter the no.of elements in the list:"))
for i in range(n):
    x=int(input("Enter the elements:"))
    alist.append(x)
e=int(input("Enter the target element:"))
pos=0
for i in range(n):
    if(alist[i]==e):
        pos=i
        print("The element is found at %d position in the list"%(pos+1))
        break
else:
     print("The element is not found")
    
