num=int(input("Enter a number: "))
temp=num
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem**3
    num=num//10

if(temp==sum):
    print("The given number is an Armstrong Number !")
else:
      print("The given number is not an Armstrong Number !")
    
    
    
