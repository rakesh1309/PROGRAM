l1=['1','2','3','4','6','7','8','5','9']
l2=['1','7','8','5','9','2','3','4','6']
for i in range(int(input())):
    n=list(input())
    if(len(n)==1):
        print("true")
    elif('0' in n):
        print('false')
    elif(len(n)==2):
        i=l1.index(n[0])
        i1=l2.index(n[1])
        if(i==i1):
            print('true')
        else:
            print('false')
    elif(len(n)==3):
        i=l1.index(n[0])
        i1=l2.index(n[2])
        if(i==i1):
            print('true')
        else:
            print('false')
    elif(len(n)==4):
        i=l1.index(n[0])
        i1=l2.index(n[3])
        i2=l1.index(n[1])
        i3=l2.index(n[2])
        
        if(i==i1 and i2==i3):
            print('true')
        else:
            print('false')
    else:
        #print('raksj')
        if(len(n)%2==0):
            i=0
            j=len(n)-1
            f=0
            #print('hi')
            #print(i,j)
            for i in range(len(n)//2):
                r1=l1.index(n[i])
                r2=l2.index(n[j])
                #print(r1,r2,i,j)
                i=i+1
                j=j-1
                if(r1==r2):
                    continue
                else:
                    f=1
                    break
                
            if(f==0):
                print('true')
            else:
                print('false')
        else:
            i=0
            j=len(n)-1
            f=0
            for i in range(len(n)//2):
                #print('od')
                r1=l1.index(n[i])
                r2=l2.index(n[j])
                #print(r1,r2,i,j)
                i=i+1
                j=j-1
                if(r1==r2):
                    continue
                else:
                    f=1
                    break
                
            if(f==0):
                print('true')
            else:
                print('false')
            
                    
