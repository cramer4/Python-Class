favorite_places = {
    "alex": "washington dc",
    "jim": "new york",
    "jenny": "tokyo"
}

for person, place in favorite_places.items():
    if place == "washington":
        print(f"{person.title()}'s favorite place is Washington DC")
    else:
        print(f"{person.title()}'s favorite place is {place.title()}")