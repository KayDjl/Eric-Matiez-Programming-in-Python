mes = "Пожалуйста укажите возраст для оценки стоимости билета на сеанс кинотеатра: "
k = ""
a = True
while a:
    k = input(mes)
    if k == "quit":
        a = False
        continue  
    try:
        k = int(k)
        if k <= 3:
            print(f"Ваш возраст: '{k}'"
                 " У вас бесплатный билет")
        elif k > 3 and k <= 12:
            print(f"Ваш возраст: '{k}'"
                " Стоимость вашего билета: 10$")
        else:
            print(f"Ваш возраст: '{k}'"
                " Стоимость вашего билета: 15$")
    except ValueError:
        print("Пожалуйста введите число или команду выхода 'quit'")
        
n = 1
while n <= 5:
    print(n)