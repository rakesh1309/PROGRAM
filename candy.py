for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if(n==1):
        print(format(l[0]/2),'.15f')
    elif(n==2):
        x=(l[0]+l[1])/2
        print(format(x,'.15f'))
    else:
        s=0
        for i in range(n-1):
            s=s+(l[i]+l[i+1])/2

        print(format(s,'.15f'))
        
