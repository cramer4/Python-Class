sandwich_orders = ["pastrami", "ham and cheese", "blt", "club", "tuna", "pastrami",
                   "grilled cheese", "sloppy joe", "reuben", "pastrami"]
finished_sandwiches = []
print("\nI'm sorry we are out of pastrami.\n\n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    making_sandwich = sandwich_orders[0]
    sandwich_orders.pop(0)
    finished_sandwiches.append(making_sandwich)
    if making_sandwich == "blt":
        print(f"I just made your {making_sandwich.upper()}.")
    else:
        print(f"I just made your {making_sandwich}.")


print("\nHere is your:")

for sandwich in finished_sandwiches:
    if sandwich == "blt":
        print(sandwich.upper())
    else:
        print(sandwich)
print("\nThank you, and have a nice day!")