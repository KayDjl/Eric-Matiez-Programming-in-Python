def city_country(city, country):
    full_country = f"{city}, {country}"
    return full_country.title()
while True:
    print("\nВведите город и страну")
    print("Если хотите завершить введите: q")
    
    cit = input('')
    if cit == 'q':
        break
    coun1 = input('')
    if coun1 == 'q':
        break
    full_city_country = city_country(cit, coun1)
    print(full_city_country)