n=raw_input()
print(n)
l=[0]*(n+1)

for q in range(int(raw_input())):
    a,b=map(int,input().split())
    low=a
    i=a
    while(i<b+1):
        l[i]=l[i]+(i-low+1)
        i=i+1
for o in range(int(input())):
    y=int(input())
    print(l[y])
