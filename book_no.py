no=int(input())
l=list(map(int,input().split()))
for i in range(int(input())):
    n=int(input())
    #print(l)
    print(l.pop(n-1))
