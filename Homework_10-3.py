def get_name():
    name = input("What's your name? ")

    with open("guest.txt", "w") as file_object:
        file_object.write(f"{name}")

get_name()