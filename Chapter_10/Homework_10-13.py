import json


filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    other = input(f"Is your name {username}? ('y', 'n') ")
    if other == "y":
        print(f"Welcome back, {username}!")
    elif other == "n":
        username2 = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username2, f)
            print(f"We'll remember you when you come back, {username2}!")