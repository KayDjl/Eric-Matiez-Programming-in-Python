from random import choice

listi = ['1', '6', '8', '7', '2', '9', 'a', 't', 'q', '4', 'h', '5', '3', 'n', '0', 'y', 'h']
print('Выиграшная комбинация 123')
writing_combo = '123'
iteration = 0
flag_imput = input('Введите количество попыток: ')
in_flad = int(flag_imput)
while in_flad > 0:
    listing = []
    for _ in range(3):
        rang = choice(listi)
        listing.append(rang)
    join_roll = ''.join(listing)
    in_flad -= 1
    iteration += 1
    print(f'Ваша комбинация: {join_roll}')
    if join_roll == writing_combo:
        print(f'ВЫ ВЫИГРАЛИ 100000$, ваша комбинация {join_roll}')
        break
else:
    print('Попытки закончиались, вы проиграли')
print(f'Количество затраченых попыток: {iteration}')
    
    

