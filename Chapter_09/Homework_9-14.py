import random
lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"]

winning_numbers = []

for number in range(0, 4):
    draw = random.choice(lottery)
    winning_numbers.append(draw)

print(winning_numbers)