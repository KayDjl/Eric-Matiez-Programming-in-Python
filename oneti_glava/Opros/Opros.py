from class_incript import AnonimnyOpros

question = 'Опрос по теме: чем вы любите заниматся\n'
my_opros = AnonimnyOpros(question)
my_opros.show_opros()
while True:
    witc = input('')
    if witc == '0':
        break
    my_opros.save_with(witc)
    
print('Спасибо за пройденый опрос.')
my_opros.self_result()

