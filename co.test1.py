for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=int(input())
    f=0
    new=[]
    if(n>=m):
        for i in range(n-1):
            n1=[]
            k=l[i]
            kk=l[i+1]
            n1.append(k+kk)
            for t in l:
                if(t!=k and t!=kk):
                    n1.append(t)
            new.append(max(n1))
                    
    else:
        f=1
    if(f==1):
        print("-1")
    else:
        print(min(new))
    
