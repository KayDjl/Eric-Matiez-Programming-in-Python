class Employe():
    
    def __init__(self, ferst_name, last_name, oklad):
        self.ferst_name = ferst_name
        self.last_name = last_name
        self.oklad = oklad
        
    def show_dialog(self):
        print(f"Работник {self.ferst_name} {self.last_name}\nОклад: {self.oklad}")
        
    def give_raise(self, priv=5000):
        self.oklad += priv
        