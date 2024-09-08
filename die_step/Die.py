from random import randint

class Die():
    def __init__(self, check1=6):
        self.check1 = check1
        
    def roll(self):
        return randint(1, self.check1)
    
