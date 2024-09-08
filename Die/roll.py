from random import randint

class Die():
    def __init__(self, num_check=6):
        self.num_check = num_check
        
    def roll(self):
        return randint(1, self.num_check)
    