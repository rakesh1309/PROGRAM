s=list(input())
n=int(input())
for i in range(len(s)):
    k=ord(s[i])
    if((k>=65 and k<=97) or (k>=97 and k<=122)):
        s[i]=chr(ord(s[i])+n)
print(''.join(s))
