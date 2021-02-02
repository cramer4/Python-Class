import json
file_name = "favorite_num.json"

with open(file_name) as f:
    favorite_num = json.load(f)
    print(f"Your favorite number is {favorite_num}")