print("Sum of Digits of Number")
n=int(input("Enter Number: "))
a,sum=n,0
if(n<0):
    n= -n
while(n>0):
    dig = n%10
    sum+=dig
    n//=10
print("Sum of digits of",a,"is",sum)
