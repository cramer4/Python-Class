taken_poll = ["bill", "george", "john", "fred", "kieth"]

favorite_numbers = {taken_poll[0]: 10,
                    taken_poll[1]: 7,
                    taken_poll[2]: 55,
                    taken_poll[3]: 30,
                    taken_poll[4]: 100}


index = 0
for friend in taken_poll:
    print(f"{friend.title()}'s favorite number is {favorite_numbers[taken_poll[index]]}")
    index = index + 1

print("\n")

poll = ["bill", "george", "john", "fred", "kieth", "bob", "tim"]

for person in poll:
    if person in taken_poll:
        print(f"Thank you {person.title()} for taking our poll!")
    else: print(f"Would you like to take our poll {person.title()}?")