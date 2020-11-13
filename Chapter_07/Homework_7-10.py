results = {}

polling_active = True
while polling_active:
    name = input("What's your name? ")
    response = input("Where would you go on your dream vacation? ")
    results[name] = response

    quit = input("Is there anyone else who will take the poll? ")
    if quit == "yes":
        print("OK\n")
    else:
        print("\nThank you all for taking this poll.\n")
        polling_active = False
print("Results:\n")

for k, v in results.items():
    print(f"{k.title()}: {v.title()}")