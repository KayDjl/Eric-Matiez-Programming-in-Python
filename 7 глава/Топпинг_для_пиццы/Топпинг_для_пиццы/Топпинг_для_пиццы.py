user = "Пожалуйста введите желаемый топинг для пиццы"
user += "\nЕсли вы сделали желаемую пиццу введите команду 'quit': "
mes = ""
list_mes = []
while mes != 'quit':
    mes = input(user)
    if mes == 'quit':
        break
    else:
        print(f"Топинг {mes} включен в заказ")
        list_mes.append(mes)
print(f"\nВы заказали пиццу со следующим желаемым набором доп топингов:")
for mes in list_mes:
    print(f"{mes}")

