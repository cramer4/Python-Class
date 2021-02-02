import json
favorite_num = input('What is your favorite number? ')
file_name = "favorite_num.json"
with open(file_name, "w") as f:
    json.dump(favorite_num, f)