from whil import full_name

print('Если хотите выйти нажмите q')
while True:
    ferste = input('Введите имя: ')
    if ferste == 'q':
        break
    laste = input('Введите фамилию: ')
    if laste == 'q':
        break
    formated = full_name(ferste, laste)
    print(formated)


