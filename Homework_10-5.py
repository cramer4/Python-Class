def get_poll():

    with open("poll_response.txt", "a") as file_object:
        while True:
            answer = input('What is your favorite thing about programing? ("q" to quit): ')
            if answer != "q":
                file_object.write(f"{answer}\n")
            else: break
get_poll()