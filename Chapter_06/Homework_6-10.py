friends = ["bill", "george", "sarah", "fred", "kieth"]

bill_favorite_numbers = [10, 35]
sarah_favortie_numbers = [55, 300]

favorite_numbers = {friends[0]: bill_favorite_numbers,
                    friends[1]: 7,
                    friends[2]: sarah_favortie_numbers,
                    friends[3]: 30,
                    friends[4]: 100}


index = 0
for friend in friends:
    print(f"{friend.title()} {favorite_numbers[friends[index]]}")
    index = index + 1