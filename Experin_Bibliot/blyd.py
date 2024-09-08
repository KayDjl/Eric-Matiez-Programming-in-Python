from random import choice

class Blyd():
    
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_diskr = choice([1, -1])
            x_distanse = choice([0, 1, 2, 3, 4])
            x_step = x_diskr * x_distanse
            
            y_diskr = choice([1, -1])
            y_distanse = choice([0, 1, 2, 3, 4])
            y_step = y_diskr * y_distanse
            
            if x_step == 0 and y_step == 0:
                continue
            
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)