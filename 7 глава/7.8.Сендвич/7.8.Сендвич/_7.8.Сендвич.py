# sandwich_orders = ['сендвич с говядиной и томантным соусом', 'pastrami',
#                    'куриный сендвич', 'pastrami', 'сендвич со свининой и '
#                    'чесночным соусом', 'pastrami']
# finiched_sandwich = []
# print('Извините но pastrami больше нет в в наличии')
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I made your tuna sandwich: {current_sandwich}")
#     finiched_sandwich.append(current_sandwich)
# print('Список всех изготовленных сендвичей')
# for fin in finiched_sandwich:
#     print(fin)

chil = {}
flag = True
while flag:
    name = input("Пожалуйста напишите ваше имя: ")
    lists = input("Укажите где бы вы хотели провести отпуск: ")
    chil[name] = lists
    
    exits = input("Хотите ли вы дальше продолжать опрос да/нет: ").lower()
    if exits == 'нет':
        flag = False
print("---- Результаты опроса ----")
for name, lists in chil.items():
    print(f"Вас зовут {name.title()} и ваш отпуск мечты - {lists.title()}")