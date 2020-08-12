import math
for _ in range(int(input())):
    m,n,k,l=input().split()
    c=1
    m=int(m)
    n=int(n)
    k=int(k)
    l=float(l)
    nn=n
    if(n>=m):
        for i in range(nn):
            if(l<=n):
                n=n-1
                l=l+l
            
    if(n<=m):            
        print(n)
    else:
        print(m)
        
