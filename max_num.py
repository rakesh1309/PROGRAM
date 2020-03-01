p1,p2,p3=map(int,input().split())
p=p1+p2+p3
l=[]
li=[]
c=0
for t in range(p):
    p=int(input())
    if(p not in l):
        l.append(p)
    elif(p in l and p not in li ):
        c=c+1
        #print("ppppp",p)
        li.append(p)
    
    

so=sorted(li)
print(c)
for i in so:
    print(i)
