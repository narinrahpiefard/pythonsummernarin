adad=input("enter you adad and amalgar:").split()
a=int(adad[0])
b=int(adad[2])
if adad[1]=="*":
    print(a*b)
elif adad[1]=="-":
    print(a-b)
elif adad[1]=="+":
    print(a+b)
elif adad[1]=="%":
    print(a%b)
elif adad[1]=="/":
    print(a/b)
elif adad[1]=="//":
    print(a//b)