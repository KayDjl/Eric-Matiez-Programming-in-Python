from random import randint
class Die():
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        ran_roll = randint(1, self.sides)
        return ran_roll
    def set_roll_die(self, sid):
        self.sides = sid