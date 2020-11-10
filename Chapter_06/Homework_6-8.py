butterscotch = {
    "animal": "dog",
    "name": "butterscotch",
    "color": "golden",
    "owner": "the marches"
}

cinnamon = {
    "animal": "hamster",
    "name": "cinnamon",
    "color": "black and white",
    "owner": "alexa"
}

lizzie = {
    "animal": "dog",
    "name": "lizzie",
    "color": "black",
    "owner": "the stebbinses"
}

pets = [butterscotch, cinnamon, lizzie]

for pet in pets:
    print(f"Animal: {pet['animal'].title()}"
          f"\nName: {pet['name'].title()}"
          f"\nColor: {pet['color'].title()}"
          f"\nOwned by: {pet['owner'].title()}\n")