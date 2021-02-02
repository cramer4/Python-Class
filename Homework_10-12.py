import json
try:
    file_name = "favorite_num.json"
    with open(file_name) as f:
        favorite_num = json.load(f)
        print(f"Your favorite number is {favorite_num}")
except FileNotFoundError:
    favorite_num = input('What is your favorite number? ')
    file_name = "favorite_num.json"
    with open(file_name, "w") as f:
        json.dump(favorite_num, f)
