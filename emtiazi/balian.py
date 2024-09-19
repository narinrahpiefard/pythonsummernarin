def calculate_floor(string):
    a = 0
    b = 0
    for i in string:
        if i == "U":
            a = a+1
        else:
            b = b+1
    d = a - b
    return (d)
print(calculate_floor(input()))
