def ToH(n,source,destination,auxiliary):
    if(n==1):
        print("Move disk 1 from source",source,"to destination",destination )
        return
    ToH(n-1,source,auxiliary,destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    ToH(n-1,destination,source,auxiliary)

n=int(input("Enter number of disks: "))
ToH(n,'A',"B","C")
