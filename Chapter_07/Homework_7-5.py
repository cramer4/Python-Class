tickets = input("Hi! How many tickets would you like to buy? ")
tickets = int(tickets)

index_1 = 1
index_2 = ""
for person in range(0, tickets):
    if index_1 == 1:
        index_2 = "st"
    elif index_1 == 2:
        index_2 = "nd"
    elif index_1 == 3:
        index_2 = "rd"
    else: index_2 = "th"
    age = input(f"What's the age of the {index_1}{index_2} person? ")
    age = int(age)
    if age < 3:
        print("The ticket is free.\n")
    elif age > 3 and age <= 12:
        print("The ticket is $10")
    elif age > 12:
        print("The ticket is $15.")
    index_1 = index_1 + 1

print("Enjoy the show!")