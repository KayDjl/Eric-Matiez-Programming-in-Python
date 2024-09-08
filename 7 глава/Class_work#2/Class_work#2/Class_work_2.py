# users_a = ['lika', 'kay', 'gerda', 'sergey']
# users_b = []
# while users_a:
#     users = users_a.pop()
#     print(f"Проверенный пользователь: {users}")
#     users_b.append(users)
# print("\nThe folowing users have been confirmed:")
# for user in users_b:
#     print(user.title())

res = {}
pol_flag = True
while pol_flag:
    name = input("Пожалуйста введите имя: ")
    games = input("Пожалуйста введите вашу любимую игру: ")
    res[name] = games
    
    repeat = input("Хотите продолжить опрос дальше да/нет: ").lower()
    if repeat == 'нет':
        pol_flag = False
        continue
        
print("---- Результаты опроса ----")
for name, games in res.items():
    print(f"Ваше имя {name.title()}, а ваша любимая игра {games.title()}")