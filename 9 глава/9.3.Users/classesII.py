from classes import User


class Privileges():
    def __init__(self, privilegs = ['Разрешено баннить пользователей', 'Разрешенно удалять пользователей',
                'Разрешенно добовлять сообщения']):
        self.priv = privilegs
    def privilegia(self):
        print('Админу предоставленны следующие аргументы: ')
        for pv in self.priv:
            print(pv)
            
class Admin(User):
    def __init__(self, first_name, last_name, *atribyts):
        super().__init__(first_name, last_name, *atribyts)
        self.priv = Privileges()