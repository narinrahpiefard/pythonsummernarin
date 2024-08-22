import random
n = random.randint(1,10)
a=0
for i in range(3):
    adad = eval(input("adad ra hads bezanid: "))
    a=a+1
    if adad == n:
        print("afarin!")
        break
    elif adad != n:
        if adad > n:
            if a<3:
                  print("lotfan adad kochak tar entekhab konid!")
        elif adad < n:
            if a < 3:
                print("lotfan adad bozorgtar ra entekhab konid!")   
if adad != n:
    print(f"shoma bakhtid! adad {n} bood!")
