import json

file_path = '../text_file/favorite_dump.json'
a = input("Введите ваше любимое число: ")
with open(file_path, 'w') as f:
    json.dump(a, f)
    
