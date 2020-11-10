jimmy = {
    "first_name": "jimmy",
    "last_name": "johnson",
    "age": 14,
    "city": "austin"
}

olivia = {
    "first_name": "olivia",
    "last_name": "carpenter",
    "age": 16,
    "city": "chicago"
}

fred = {
    "first_name": "fred",
    "last_name": "jones",
    "age": 15,
    "city": "boston"
}

people = [jimmy, olivia, fred]

for person in people:
    print(f"Full name: {person['first_name'].title()} {person['last_name'].title()}"
          f"\nage: {person['age']}\ncity {person['city'].title()}\n")