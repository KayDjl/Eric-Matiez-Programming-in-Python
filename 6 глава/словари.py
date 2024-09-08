lika = {
    'name': 'Анжелика',
    'family': 'Югова',
    'age': '19',
    'city': 'Лермонтов',
}
print (lika['name'])
print (lika['family'])
print (lika['age'])
print (lika['city'])

favorite_numbers = {
    'lika': '19',
    'sergey': '4',
    'mom': '3',
    'dad': '1',
}
print(f"Lika is favorite numbers {favorite_numbers['lika']}")
print(f"Sergey is favorite numbers {favorite_numbers['sergey']}")
print(f"Mom is favorite numbers {favorite_numbers['mom']}")
print(f"Dad is favorite numbers {favorite_numbers['dad']}")

glas = {
    'Константа': 'это переменная, значение которой нельзя изменить',
    'pep_8': 'это общепризнаный набор патернов, структур рекомендуемых для всех программистов python',
    'If_Else': 'это функция проверки логического условия если',
    'print': 'это команда для вывода текста при компиляции кода',
    'for': 'это функция цикла, позволяет перебрать элементы списка, словаря и тп'
}
for key, value in glas.items():
    print(f'\n{key}:\n{value}')
