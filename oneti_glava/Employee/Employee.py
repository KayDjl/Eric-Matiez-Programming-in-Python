from class_employee import Employe

while True:
    name = input('Введите ваше имя: ')
    if name == '0':
        break
    last = input('Введите вашу фамилию: ')
    if last == '0':
        break
    oklad = input('Введите ваш оклад: ')
    if oklad == '0':
        break
    else:
        oklad = int(oklad)
        
    my_rab = Employe(name, last, oklad)
    my_rab.show_dialog()
    my_rab.give_raise(7000)
    my_rab.show_dialog()