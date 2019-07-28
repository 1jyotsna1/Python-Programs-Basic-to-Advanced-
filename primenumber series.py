def isPrime(y):
  i=2
  while(i<y):
    if(y%i==0):
      return 0
      exit()
    i=i+1
  return 1

x=int(input("Enter a number"))
count=1
n=2
while(count<=x):
    if(isPrime(n)==1):
        print(n)
        count+=1
    n=n+1

        

'''
n=int(input("Enter a number: "))
for a in range(2,n+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)
'''
