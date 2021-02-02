def get_names():

    with open("guest_list.txt", "a") as file_object:
        while True:
            name = input('What is your name? ("q" to quit): ')
            if name != "q":
                file_object.write(f"{name}\n")
            else: break
get_names()