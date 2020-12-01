import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        number = random.randint(1, self.sides)
        print(number)

six_sided_die = Die()
six_sided_die.roll()
ten_sided_die = Die(sides=10)
ten_sided_die.roll()
twenty_sided_die = Die(sides=20)
twenty_sided_die.roll()