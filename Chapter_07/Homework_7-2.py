question = 0
while question == 0:
    party = input("Welcome to our restaurant! How many people are in your party? ")

    party = int(party)
    if party <= 8 and party > 0:
            print("We have a table ready for you!")
            question = 1
    elif party > 8 and party <= 20:
            print("Please wait a few minutes while we prepare a table.")
            question = 1
    elif party > 20:
            print("I apologize, we do not have a table that big.")
            question = 1
    else:
        print("Please type the number of people in your party.")
