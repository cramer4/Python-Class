import random
lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"]

your_ticket = [1, 2, 3, 4]
winning_numbers = []
tries = 0
while your_ticket != winning_numbers:
    for number in range(0, 4):
        draw = random.choice(lottery)
        winning_numbers.append(draw)

    print(winning_numbers)
    tries = tries + 1
    if your_ticket == winning_numbers:
        print("You Win.")
        break
    else: winning_numbers = []

print(f"It took {tries} tickets to win")