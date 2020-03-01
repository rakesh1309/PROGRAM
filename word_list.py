li=''
d=["'",'.',",",';',':']
for i in range(int(input())):
    l=input()
    li=li+' '+l
k=li.lower()

k=sorted(set(k.split()))
print(len(k))
#print(k)
s=' '.join(k)
for i in d:
    s=s.replace(i," ")
s=s.split()
for i in s:
    print(i)



