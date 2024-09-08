import json

def load_number():
    try:
        filename = '../text_file/favorite_dumps.json'
        with open(filename) as f:
            contecst = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return contecst
    
def dump_numbers():
    fav_num = input("Введите ваше любимое число: ")
    filename = '../text_file/favorite_dumps.json'
    with open(filename, 'w') as f:
        json.dump(fav_num, f)
    return fav_num
def fav_numbers():
    fav = load_number()
    if fav:
        print(f"Я знаю ваше любимое число! Это {fav}")
    else:
        fav = dump_numbers()
        print(f"Я знаю ваше любимое число!!! Это {fav}")
        
fav_numbers()
    