while True:
    command = input(">>").split()
    a = command[0]
    if a == "Add":
        file = open("phonebook_new.txt","a")
        name = command[1]
        phone = command[2]
        file.write(f"\n{name}:{phone}")
        file.close
    elif a == "Show":
        file = open("phonebook_new.txt","r")
        data = file.read()
        print(data)
        file.close
    elif a == "Edit":
        file = open("phonebook_new.txt","r")
        data = file.read().split()
        name1 = input("enter number and name you want to edit: ")
        if name1 in data:
            for i in data:
                if name1 in i:
                    data.remove(i)
            file = open("phonebook_new.txt","w")
            command7 = input("enter new name and number: ")
            for i in data:
                file.write(i+"\n")
            file.write(command7)
        else:
            print("we dont have this name or number")
        file.close
    elif a == "Delete":
        file = open("phonebook_new.txt","r")
        data = file.read().split()
        name2 = input("enter name and number you want to delete: ")
        if name2 in data:
            for i in data:
                if name2 in i:
                    data.remove(i)
            file = open("phonebook_new.txt","w")
            for i in data:
                file.write(i+"\n")
            file.close
        else:
            print("we dont have this name or number")
    elif a == "Block":
        file = open("phonebook_new.txt","r")
        data = file.read().split()
        name3 = input("enter name and number you want to delete: ")
        if name3 in data:
            file.close
            file = open("blocked.txt","r")
            data = file.read().split()
            data.append(name3)
            print(f"{name3} blocked.")
        else:
            print("we dont have this name or number")
        file.close
    elif a == "Call":
        file = open("phonebook_new.txt","r")
        data = file.read().split()
        name4 = input("enter name and number you want to call: ")
        if name4 in data:
            print(f"calling {name4}...!")
        else:
            print("we dont have this name or number")
        file.close
        