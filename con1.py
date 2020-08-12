for _ in range(int(input())):
    n,a,b,c=map(int,input().split())
    m=min(list(map(int,input().split())))
    
    if(a<b):
        print((m-b)+(m-a)+(c))
    elif(b<a and m <a):
        print((a-b)+c)
    else:
        print(a-b)
    
