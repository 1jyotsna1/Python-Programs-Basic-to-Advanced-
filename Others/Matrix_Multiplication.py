A=[[6,5,3],[9,5,7],[1,2,3]]

B=[[8,8,12,2],[2,9,6,10],[1,2,7,4]]

R=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for p in range(len(A)):
    for q in range(len(B[0])):
        for r in range(len(B)):
            R[p][q]+=A[p][r]*B[r][q]
for a in A:
    print(a)
    
print("\n")

for b in B:
    print(b)
    
print("\n")

print("The multiplication of 2 matrices is")
    
for res in R:
    print(res)


