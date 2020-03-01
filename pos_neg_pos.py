for _ in range(int(input())):
    n=int(input())
    l=[]
    l=list(map(int,input().split()))
    for i in range(n):
        if(l[i]<0):
            l[i]=0
        elif(l[i]>0):
            l[i]=1
    print("ll",l)
    r=[1]*n
    count=1
    for i in range(n-2,-1,-1):
        if l[i]!=l[i+1]:
            r[i]=r[i+1]+1
    for i in range(n):
        print(r[i],end=' ')
    print()
        
