#Считаем до 20
#for number in range(1,20):
 #   print(number)
#Милионы
#milions = list(range(1, 1_000_000))
#for milion in milions:
    #print(milion)


#Суммирование милионна 
#mils = list(range(1, 1_000_000))
#mins = min(mils)
#print(mins)

#maxs = max(mils)
#print(maxs)

#sums = sum(mils)
#print(sums)
#print(mils)

#Нечетные числа
Not_nubers = list(range(1, 20, 2))
for nots in Not_nubers:
    print(nots)

#Тройки
values = []
for value in range(3, 30, 3):
    values.append(value)
print(values)

#Кубы
xes = []
for cub in range(1, 10):
    cube = cub**3
    xes.append(cube)
print(xes)

#Генератор кубов
jes = [namb**3 for namb in range(1,10)]
print(jes)