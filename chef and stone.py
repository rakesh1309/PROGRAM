for _ in range(int(input())):
    a,b,m=map(int,input().split())
    m1=(m*(m+1))//2
    i=min(m1,a,b)
    r=a+b-(2*i)
    print(r)
