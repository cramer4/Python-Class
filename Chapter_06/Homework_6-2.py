friends = ["bill", "george", "sarah", "fred", "kieth"]

favorite_numbers = {friends[0]: 10,
                    friends[1]: 7,
                    friends[2]: 55,
                    friends[3]: 30,
                    friends[4]: 100}


index = 0
for friend in friends:
    print(f"{friend.title()} {favorite_numbers[friends[index]]}")
    index = index + 1