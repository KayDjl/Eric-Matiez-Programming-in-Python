def alboms(name_musik, name_albom, name_musik1, name_albom1, name_musik2, name_albom2, jaker = None, Jaker1 = None, Jaker2 = None):
    albom1 = {'Исполнитель': name_musik, 'Название': name_albom}
    if jaker:
        albom1['Дорожка'] = jaker
    albom2 = {'Исполнитель': name_musik1, 'Название': name_albom1}
    if Jaker1:
        albom2['Дорожка'] = Jaker1
    albom3 = {'Исполнитель': name_musik2, 'Название': name_albom2}
    if Jaker2:
        albom3['Дорожка'] = Jaker2
    return albom1, albom2, albom3

flag = True
while flag:
    print("Если хотите выйти то введите 'q'")
    al = input("Введите имя исполнителя: ")
    if al == 'q':
        flag = False
        continue
    aln = input("Введите название альбома: ")
    if aln == 'q':
        flag = False
        continue
    jk = input("Введите дорожку первого альбома если она есть если нету нажмите 'enter': ")
    if jk =='q':
        flag = False
        continue
    elif jk == None:
        continue
    al1 = input("Введите имя исполнителя#2: ")
    if al1 == 'q':
        flag = False
        continue
    aln1 = input("Введите название альбома#2: ")
    if aln1 == 'q':
        flag = False
        continue
    jk1 = input("Введите дорожку второго альбома если она есть если нету нажмите 'enter': ")
    if jk =='q':
        flag = False
        continue
    al2 = input("Введите имя исполнителя#3: ")
    if al2 == 'q':
        flag = False
        continue
    aln2 = input("Введите название альбома#3: ")
    if aln2 == 'q':
        flag = False
        continue
    jk2 = input("Введите дорожку третьего альбома если она есть если нету нажмите 'enter': ")
    if jk =='q':
        flag = False
        continue
    elif jk == None:
        continue
    print()
    full_alboms = alboms(al, aln, al1, aln1, al2, aln2, jaker = jk, Jaker1 = jk1, Jaker2 = jk2)
    for albm in full_alboms:
        print(albm)

    