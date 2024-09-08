from pyexpat.errors import messages


number = 1
while number <=5:
    print(number)
    number += 1

prom = "\nИгра в сообщение"
prom += "\nЕсли вы хотите остановить игру введите 'exit'"
activ = True
while activ:
    message = input(prom)
    if message == 'exit':
        activ = False
    elif message == "10":
        activ = False
    else:
        print(message)
    



        