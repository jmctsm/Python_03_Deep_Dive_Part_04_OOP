def line_break():
    x = 0
    print("\n\n")
    while x < 20:
        print("*", end="")
        x += 1
    print("\n\n")

line_break()

from datetime import datetime

class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.utcnow().isoformat()

class Logger:
    current_time = TimeUTC()

print(f'Logger.__dict__ = {Logger.__dict__}')

l = Logger()
print(f'l.current_time = {l.current_time}')

line_break()

from random import choice, seed

class Deck:
    @property
    def suit(self):
        return choice(('Spade', 'Heart', 'Diamond', 'Club'))

    @property
    def card(self):
        return choice(tuple('23456789JQKA') + ('10',))

d = Deck()
seed(0)
for _ in range(10):
    print(d.card, d.suit)

line_break()

class Choice:
    def __init__(self, *choices):
        self.choices = choices

    def __get__(self, instance, owner_class):
        return choice(self.choices)

class Deck:
    suit = Choice('Spade', 'Heart', 'Diamond', 'Club')
    card = Choice(*'23456789JQKA', '10')

seed(0)
d = Deck()
for _ in range(10):
    print(d.card, d.suit)

line_break()

class Dice:
    die_1 = Choice(1,2,3,4,5,6)
    die_2 = Choice(1,2,3,4,5,6)
    die_3 = Choice(1,2,3,4,5,6)

seed(0)
dice = Dice()
for _ in range(10):
    print(dice.die_1, dice.die_2, dice.die_3)
