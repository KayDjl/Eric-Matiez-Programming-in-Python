def city_full(city, strana, nasil=''):
    if nasil:
        full = f'{city.title()}, {strana.title()} - популяция {nasil.title()}'
    else:
        full = f'{city.title()}, {strana.title()}'
    return full