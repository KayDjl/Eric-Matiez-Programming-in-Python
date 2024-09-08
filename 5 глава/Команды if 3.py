list_users = ['sergey', 'lika', 'sem', 'kay', 'gerda', 'jorik', 'admin']
if not list_users:
    print('Список пустой')
for list_user in list_users:
    if list_user == 'admin':
        print('Hello, admin, would you like to see a status report?')
    else:
        print('Hello, my family, thank you for logging in again')


current_users = ['alisa', 'maikal', 'jori', 'pepo', 'keri']
new_users = ['yre', 'yri', 'jori', 'tati', 'KERI']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('Такое имя пользователя уже используется')
    else:
        print('Имя пользователя свободно')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")