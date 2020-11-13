
def order_v1():
    print("What is the first topping you'd like on your pizza?\n"
          "Enter 'quit' when you are finished.")
    topping = ""
    toppings = []
    while topping != "quit":
        topping = input("Topping: ")
        if topping == "quit":
            break
        else:
            print(f"Added {topping} to your pizza.")
            toppings.append(topping)
    print("\nThat's a pizza with:")
    for item in toppings:
        print(f"{item}")
    correct = ""
    while correct != "yes" or "no":
        correct = input("Is that correct? ")
        if correct == "yes":
            print("\nYour pizza will be ready soon. Have a nice day!")
            break
        elif correct == "no":
            print("\nI'm sorry, we'll try again.\n\n")
            order_v1()
        else:
            print("Please type 'yes' or 'no'.")

def order_v2():
    print("What is the first topping you'd like on your pizza?\n"
          "Enter 'quit' when you are finished.")
    topping = ""
    toppings = []
    while topping != "quit":
        topping = input("Topping: ")
        if topping == "quit":
            topping = "quit"
        else:
            print(f"Added {topping} to your pizza.")
            toppings.append(topping)
    print("\nThat's a pizza with:")
    for item in toppings:
        print(f"{item}")
    correct = ""
    while correct != "yes" or "no":
        correct = input("Is that correct? ")
        if correct == "yes":
            print("\nYour pizza will be ready soon. Have a nice day!")
            break
        elif correct == "no":
            print("\nI'm sorry, we'll try again.\n\n")
            order_v2()
        else:
            print("Please type 'yes' or 'no'.")

def order_v3():
    print("What is the first topping you'd like on your pizza?\n"
          "Enter 'quit' when you are finished.")
    topping = ""
    toppings = []
    running = True
    while running:
        topping = input("Topping: ")
        if topping == "quit":
            running = False
        else:
            print(f"Added {topping} to your pizza.")
            toppings.append(topping)
    print("\nThat's a pizza with:")
    for item in toppings:
        print(f"{item}")
    correct = ""
    while correct != "yes" or "no":
        correct = input("Is that correct? ")
        if correct == "yes":
            print("\nYour pizza will be ready soon. Have a nice day!")
            break
        elif correct == "no":
            print("\nI'm sorry, we'll try again.\n\n")
            order_v3()
        else:
            print("Please type 'yes' or 'no'.")

version = ""
while version != 1 or 2 or 3:
    version = input("Do you want to run version 1, 2, or 3? ")
    if version == "1":
        order_v1()
        break
    elif version == "2":
        order_v2()
        break
    elif version == "3":
        order_v3()
        break
    else:
        print("Please type 1, 2, or 3.")