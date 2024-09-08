from os import write


path = '../text_file/guest_books1.txt'
flag = True
while flag:
    gos = input('Для выхода введите:q\n'
               'Введите ваше имя: ')
    op = input('Расскажите почему вам нравится программировать: ')
    if gos == 'q' or op == 'q':
        flag = False
        continue
    else:
        opros = f'Меня зовут {gos}, мне нравится программировать потому что: {op}'
        with open(path, 'a') as file:
            file.write(f'{opros}\n')
        
