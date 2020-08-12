n=int(input())
l=[]
for i in range(n):
    a,c=map(int,input().split())
    k1=[x for x in range(a,c+1)]
    l.append(k1)
#print(l)
q=int(input())
for i in range(q):
    b=list(map(int,input().split()))
    copy=l
    #print("copy",copy)
    a1=b[0]
    a2=b[1:]
    #print(a1,a2)
    c=0
    e=[]
    for h in range(a1):
        w1=a2[h]
        #print(w1)
        for p in copy:
            if( w1 in p and p not in e):
                c=c+1
                #print("r")
                e.append(p)

        

        
    print(c)
        
        
        
