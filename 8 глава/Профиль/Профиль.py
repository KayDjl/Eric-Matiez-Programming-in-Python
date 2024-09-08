from tkinter import OFF


def profile(ferst, last, **kwargs):
    kwargs['ferst_name'] = ferst
    kwargs['last_name'] = last
    return kwargs
    

failde = profile('Sergey', 'Polozkov', location='Lermontov', field = 'Programer', age = 11)
print(failde)

def avto_salon(proizvod, model, **lists):
    lists['proizvoditel'] = proizvod
    lists['model_raid'] = model
    return lists
off_top = avto_salon('Nissan', 'Skyline R-34', color = 'blue', dvigatel = 'JZ-2', pakets = True)
print(off_top)