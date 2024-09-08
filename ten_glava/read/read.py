import os

with open('pi.txt') as file_object:
    contecst = file_object.read()
print(contecst.rstrip())

print(f"Текущий рабочий каталог: {os.getcwd()}")






path = '../text_file/pi2.txt'
with open(path) as file_object1:
    contecst1 = file_object1.readlines()
    
print(contecst1)
pi_string = ''
for line in contecst1:
    pi_string += line.rstrip()
berday = input("Введите дату роождение: ")
if berday in pi_string:
    print("Входит в 100 знаков после запятой")
else:
    print("Не входит в 100 знаков после запятой")