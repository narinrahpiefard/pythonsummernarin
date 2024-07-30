speed=eval(input("enter your speed: "))
if speed < 90:
    print("no ticket!")
elif speed >= 91 and speed < 110:
    print("small ticket!")
else:
    print("big ticket!")