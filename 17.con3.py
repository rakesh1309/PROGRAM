def pro(myList) : 
    result = 1
    for x in myList: 
         result = result * x  
    return result

for _ in range(int(input())):
    li=[]
    n=int(input())
    for i in range(1,n+1):
        if(n%i==0):
            li.append(i)
    #print(li)
    s1=sum(li)
    p1=pro(li)
    #print(s1,p1)

    c=0
    for i in range(len(li)-1):
        a=li[i]
        #print(a,'aa')
        for t in range(i+1,len(li)):
            c=c+(a*li[t])
            #print(a,li[t],a*li[t])
    print(c+s1+p1)
