def separator(ls):
    zoj = []
    fard = []
    for i in ls:
        if i % 2 == 0:
            zoj.append(i)
        else:
            fard.append(i)
    return (f"{zoj} , {fard}")
a = eval(input("enter numbers: "))
print(separator(a))
