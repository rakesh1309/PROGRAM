for i in range(int(input())):
    a=list(input())
    b=list(input())

    sa=list(sorted(set(a)))
    sb=sorted(b)
    m=min(len(sa),len(sb))
    print(sa,sb,m)
    res=list(sa^sb)
    print(res)


    
    '''m=min(len(sa),len(sb))
    ma=max(len(sa),len(sb))
    print(sa,sb,m)
    c=0
    for i in range(m):
        if(sa[i]==sb[i]):
            continue
        else:
            c=c+1
    print(c)
    print(c+ma-m)'''
