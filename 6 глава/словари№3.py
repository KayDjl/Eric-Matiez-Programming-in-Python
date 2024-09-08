lika = {
    'name': 'Анжелика',
    'family': 'Югова',
    'age': '19',
    'city': 'Лермонтов',
}

sergey = {
    'name': 'Сергей',
    'family': 'Полозков',
    'age': '24',
    'city': 'Лермонтов',
}

kay = {
    'name': 'Кай',
    'family': 'Полозков',
    'age': '1',
    'city': 'Лермонтов',
}

people = [lika, sergey, kay]

for peopl in people:
    print(peopl)
print('\n')

kay1 = {
    'vid': 'cat',
    'vladelech': 'sergey and lika',
}
gerda = {
    'vid': 'cat_women',
    'vladelech': 'sergey and lika',
}

pets = [kay1, gerda]
for pet in pets:
    print(pet)
print('\n')

favorite_places = {
    'bechtay': 'sergey',
    'karier': 'lika',
    'kyhnia': 'kay',
}
for name, mesto in favorite_places.items():
    print(f"{name} is favorite places {mesto}")
print('\n')

favorite_numbers = {
    'lika': [19, 4, 3],
    'sergey': [11, 4, 9],
    'mom': [1, 7],
    'dad': [0, 1],
}
for name, numbers in favorite_numbers.items():
    print(f'Favorite numbers {name} is:')
    for numbe in numbers:
        print(f"\t{numbe}")
print('\n')

cities = {
    'lermontov': {
        'country': 'russian',
        'population': 12000,
        'fact': "Это город с богатыми местами миниральных вод и горами такими"
         "как бештау, остренькая, шелудивая. Является городом курортом",
    },

    'pyatigorsk': {
        'country': 'russian',
        'population': 39000,
        'fact': "Является городом с богатой историей, историческими зданиями,"
        " так же тут находится гора машук с канатной дорожкой",
    },
}
for name, info in cities.items():
    print(f"\n{name.title()}:")
    city = f"{info['country'].title()}"
    popul = f"{info['population']}"
    info_city = f"{info['fact']}"
    print(f'Country: {city}')
    print(f'Population: {popul}')
    print(f'Fact: {info_city}')

