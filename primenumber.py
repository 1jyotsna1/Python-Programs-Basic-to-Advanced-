while True:
    n=int(input("Enter a number"))
    i=2
    while(i<=n-1):
        if(n%i==0):
            print("Not a prime number")
            break
        i=i+1
    if(i==n):
        print("Prime number")
    another=input("Want to enter another number? ('y' for Yes, any other key press to discontinue: ")
    if(another!='y'):
        break
