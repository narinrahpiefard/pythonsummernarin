radif=input("vaziat sandali haro vared konid: ").split()
radif1=input("vaziat sandali haro vared konid: ").split()
a=0
for i in range(8):
    if radif[i]==radif1[i] and radif[i]!="0" and radif1[i]!="0":
        a=a+1
print(a)