def rec(x):
    if(x==1):
        return(1)
    else:
        f=x*rec(x-1)
    return(f)


'''
def factorial(x):
    f=1
    for i in range(x,1,-1):
        f=f*i
    return(f)
'''

n=int(input("Enter a number"))
print("Factorial value is",rec(n))
