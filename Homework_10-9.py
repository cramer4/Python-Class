def get_cats():
    try:
        file_name = "cats.txt"
        with open("cats.txt") as cat_file:
            cat_names = cat_file.read()
            print(cat_names)
    except FileNotFoundError:
        pass

def get_dogs():
    try:
        file_name = "dogs.txt"
        with open("dogs.txt") as dog_file:
            dog_names = dog_file.read()
            print(dog_names)
    except FileNotFoundError:
        pass


get_cats()
print("")
get_dogs()