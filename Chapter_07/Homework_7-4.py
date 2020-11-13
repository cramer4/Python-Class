def order():
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
            order()
        else:
            print("Please type 'yes' or 'no'.")
order()