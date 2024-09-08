from whike import city_full

while True:
    cit = input('Введите город: ')
    if cit == 'q':
        break
    star = input('Введите странну: ')
    if star == 'q':
        break
    nas = input('Введите насиление города: ')
    fulled = city_full(cit, star, nas)
    print(fulled)
    
