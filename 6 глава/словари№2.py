city_river = {
    'nile': 'egypt',
    'baikal': 'siberia',
    'kama': 'permi'
}
for k, v in city_river.items():
    print(f'The {k} runs through {v}')
print("\n")
for k in city_river.keys():
    print(f"The {k.title()}")
print("\n")
for v in city_river.values():
    print(f'runs {v.title()}')


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

opros = ['sergey', 'jen', 'lika', 'phil', 'kay', 'sarah']
print("\n")
for name in favorite_languages.keys():
    print(f'Hello {name}')
    if name in opros:
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, вы уже прошли опрос, ваш любимый язык {language}')
for name in opros:
        if name not in favorite_languages:
            print(f'Hello {name}, не хотели бы вы пройти опрос?')

