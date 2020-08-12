import datetime 
import calendar
from datetime import date, timedelta
def findday(da): 
    day, month, year = (int(i) for i in da.split('-'))     
    daynumber = calendar.weekday(year, month, day) 
    days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
    return (days[daynumber]) 
   



fi=open("input.txt","w+")
l,ll=input().split()
#print(l,ll)
fi.write(l)
fi.write(' ')
fi.write(ll)
fi.close()
fi=open("input.txt","r+")
fo=open("output.txt","w+")
r=fi.read()
date=list(r.split())
#print(date)
d1=date[0]
d2=date[1]
d11=d1.split("/")
d12=d2.split("/")
#print(d1,d11)
#print(d1,d12)
df='%d/%m/%Y'
c=0
flag=0
if(datetime.datetime.strptime(d1, df) and datetime.datetime.strptime(d2, df)):
    if(d11[0]<d12[0]):
        if(int(d11[0])>30 and int(d11[1])>12 or int(d11[2])>2019 and int(d12[0])>30 and int(d12[1])>12 or int(d12[2])>2019):
    
            nc=int(d12[0])-int(d11[0])
            #print("omber to day",nc)
            n=int(d11[0])
            n1=int(d12[0])
            #print("nc",nc,n,n1)
            p=int(d11[1])
            pp=int(d11[2])
            #print(p,pp)

            
            for i in range(n,n1+1):
                
                #print("date",i)
                new=datetime.date(pp,p,i)
                print(list(new))
                if(findday(new)!="Sunday" or findday(new)!="Saturday"):
                    c=c+1
                n=n+1
            #print(c)
        else:
            flag=1
    else:
        flag=1
else:
    flag=1
                   
if(flag==1):
    fo.write("invalid")
    #print("invalid")
else:
    fo.write(str(c))
    #print('count',c)                
        
    
    






fo.close()
fi.close()
