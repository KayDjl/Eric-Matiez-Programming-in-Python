class User():
    def __init__(self, first_name, last_name, *atribyts):
        self.first_name = first_name
        self.last_name = last_name
        self.atribyts = atribyts
        self.login_users = 0
        
    def describe_user(self):
        print(f"Пользователь: {self.first_name} {self.last_name}")
        print(f"Характеристика пользователя: ")
        for atr in self.atribyts:
            print(f"- {atr}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")
    def increment_login_user(self, log = 1):
        self.login_users += log
    def reset_login_users(self, reset = 0):
        self.login_users = reset
        
