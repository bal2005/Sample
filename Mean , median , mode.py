def mean(list,n):
    get_sum=sum(list)
    mean=get_sum/n
    return mean
def median(list,n):
    if(n//2==0):
        median1=list[n//2]
        median2=list[n//2]-1
        median=median1+median2//2
    else:
        median=list[n//2]
    return median
def mode(list):
    fre={ }
    for i in a:
        fre.setdefault(i,0)
        fre[i]+=1
    highfre=max(fre.values())
    high=[ ]
    for n,k in fre.items():
        if k==highfre:
            high.append(n)
    return high
a=[ ]
n=int(input("Enter size of the list : "))
for i in range(n):
    a.append(int(input("Enter elements: ")))
print("Mean of the given list is",mean(a,n))
print("Median of the given list is",median(a,n))
print("Mode of the given list is",mode(a))
