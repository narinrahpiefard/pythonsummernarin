contacts = {}
blocked = []

while True:
    command = input(">>")
    command_list = command.split()
    a = command_list[0]
    if a == "add":
        name = command_list[1]
        phone = command_list[2]
        contacts[name] = phone
    elif a == "show":
        for i in contacts:
            print(i,contacts[i])
    elif a == "edit":
        c = input("Edit name or phone?")
        if c == "phone":
            name = input("Enter contacts name:")
            if name in contacts.keys():
                new_phone = input("Please Enter new phone number:")
                contacts[name] = new_phone
            else:
                print("Sorry!We dont have this name.")
        else:
            name = input("Enter contacts name:")
            if name in contacts.keys():
                new_name = input("Enter contacts new name:")
                contacts[new_name] = contacts[name]
                del contacts[name]
            else:
                print("Sorry!We dont have this name.")

    elif a == "delete":
        name = input("Enter contacts name:")
        if name in contacts.keys():
            del contacts[name]
        else:
            print("Sorry!We dont have this name.")

    elif a == "block":
        name = input("Enter contacts name:")
        if name in contacts.keys():
            blocked.append(name)
            print(f"{name} blocked.")
        else:
            print("Sorry!We dont have this name.")
    elif a == "call":
        name = input("Enter contacts name:")
        if name in contacts.keys():
            if name in blocked:
                print("This number has been blocked!")
                choice = input(f"Do you want to unblock {name}?(y/n)")
                if choice == "y":
                    blocked.remove(name)
                    print(f"Calling {contacts[name]} ...")
                else:
                    pass
            else:
                print(f"Calling {contacts[name]} ...")

        else:
            print("Sorry!We dont have this name.")
