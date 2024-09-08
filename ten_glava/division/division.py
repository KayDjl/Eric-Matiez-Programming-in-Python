# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Делить на ноль нельзя")

print("Калькулятор деления")
while True:
    w_nuber = input("Введите число: ")
    if w_nuber == 'q':
        break
    s_number = input("Введите делитель: ")
    if s_number == 'q':
        break
    try:
        aws = int(w_nuber) / int(s_number)
    except ZeroDivisionError:
        print("Делить на ноль нельзя")
    else:
        print(f"Результат: {int(aws)}")