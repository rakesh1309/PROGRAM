s=input("Enter Your String:")
vo=('aeious')
s=s.lower()
for x in s:
        if x in vo:
                s=s.replace(x,"")
                print(s)
