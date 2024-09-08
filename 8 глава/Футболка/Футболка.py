def make_shirt(size = "L", inf = 'I love python'):
    print(f"Футболка {size} размера")
    print(f"Надпись на футболке: {inf}\n")
make_shirt()
make_shirt(inf = 'Я люблю программирование', size = 'M')
    
def descrite_city(city, strana = 'russian'):
    print(f"{city.title()} is in {strana.title()}\n")
descrite_city(city = 'moskow')
descrite_city('st. pesherburg')
descrite_city('boston', 'america')
