rivers = {
    "mississippi river": "usa",
    "amazon river": "brazil",
    "mekong river": "china",
}

for key, value in rivers.items():
    if value == "usa":
        print(f"The {key.title()} runs through the {value.upper()}")
    else:
        print(f"The {key.title()} runs through {value.title()}")

print("\n")
print("The rivers are:\n")

for key in rivers:
    print(f"The {key.title()}")

print("\n")
print("The countries are:\n")

for value in rivers.values():
    if value == "usa":
        print(f"The {value.upper()}")
    else:
        print(value.title())