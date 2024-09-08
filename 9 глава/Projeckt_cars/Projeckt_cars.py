class Car():
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
        self.probeg = 0
        
    def lists(self):
        log_list = f"{self.model} {self.make} {self.year}"
        return log_list.title()
    
    def out_probeg(self):
        print(f"Пробег данной машины составляет {self.probeg} км")
        
    def update_probeg(self, milies):
        if milies >= self.probeg:
            self.probeg = milies
        else:
            print("Пробег не может быть меньше текущего")
            
class Bettery():
    def __init__(self, bettery_size=75):
        self.bettery_size = bettery_size
    def discribe_bettery(self):
        print(f"Емкость аккумулятора равна {self.bettery_size} - kWh")
    def set_bettery_size(self, size):
        self.bettery_size = size
    def upgrade_battery(self):
        if self.bettery_size <= 75:
            moch = 100
        elif self.bettery_size > 75 and self.bettery_size <= 100:
            moch = 150
        else:
            moch = 200
        print(f"Мощность данной машины составляет {moch}")
        
class ElectroCar(Car):
    def __init__(self, model, make, year):
        super().__init__(model, make, year)
        self.bettery = Bettery()
        
my_electr_car = ElectroCar('X5', 'tesla', '2024')
print(my_electr_car.lists())
my_electr_car.bettery.discribe_bettery()
you_electr_car = ElectroCar('jaja', 'Popi', '2030')
you_electr_car.bettery.set_bettery_size(150)
print(you_electr_car.lists())
you_electr_car.bettery.discribe_bettery()
my_electr_car.bettery.upgrade_battery()
you_electr_car.bettery.upgrade_battery()
