sandwich_orders = ["ham and cheese", "blt", "club", "tuna", "grilled cheese", "sloppy joe", "reuben", "pastrami"]
finished_sandwiches = []

while sandwich_orders:
    making_sandwich = sandwich_orders[0]
    sandwich_orders.pop(0)
    finished_sandwiches.append(making_sandwich)
    if making_sandwich == "blt":
        print(f"I just made your {making_sandwich.upper()}.")
    else:
        print(f"I just made your {making_sandwich}.")


print("\nI made your:")

for sandwich in finished_sandwiches:
    if sandwich == "blt":
        print(sandwich.upper())
    else:
        print(sandwich)
