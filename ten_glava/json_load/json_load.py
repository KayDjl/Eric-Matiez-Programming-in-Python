import json

def read_username():
    filename = '../text_file/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def great_user():
    username = input('Введите ваше имя: ')
    filename = '../text_file/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
            
def list_user():
    cont = read_username()
    if cont:
        pas = input(f"Ваше имя {cont}, правильно ли это? Ответьте да/нет: ").lower()
        if pas == 'да':
            print(f'Приветствуем вас {cont}')
        elif pas == 'нет':
            cont = great_user()
            print(f"Приветствуем вас {cont}")
    else:
        cont = great_user()
        print(f"Мы сохранили ваше имя {cont}")
        
list_user()
            