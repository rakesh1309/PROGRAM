import math
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    div=(10*n)*math.pi
    p=(1/div)*s
    print(p)
