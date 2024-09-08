class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Ресторан {self.restaurant_name} предлагает {self.cuisine_type} кухню")
        
    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт")
    def set_number_served(self, served):
        self.number_served = served
    def increment_number_served(self, serv):
        self.number_served += serv
        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    def lists_flavors(self):
        print("Список сортов мороженного:")
        for flav in self.flavors:
            print(flav)