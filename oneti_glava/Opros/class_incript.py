class AnonimnyOpros():
    def __init__(self, witch):
        self.witch = witch
        self.listion = []
        
    def show_opros(self):
        print(self.witch)
    
    def save_with(self, new_with):
        self.listion.append(new_with)
        
    def self_result(self):
        print('Результаты опроса:')
        for lists in self.listion:
            print(f'- {lists}')