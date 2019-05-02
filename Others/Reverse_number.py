r=0
m=input("Enter a number ")
n=int(m)
while n!=0:
    a=n%10
    r=r*10+a
    n=n//10
    

print("The reverse number is",r)



