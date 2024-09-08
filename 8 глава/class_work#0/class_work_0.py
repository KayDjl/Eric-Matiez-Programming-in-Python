def fav_name(ferst_name, midle_name, last_name=''):
    if fav_name:
        full_name = f"{ferst_name} {midle_name} {last_name}"
    else:
        full_name = f"{ferst_name} {last_name}"
    return full_name.title()

musical = fav_name('Jon', 'Sina')
print(musical)

musical = fav_name('jon', 'sina', 'arab')
print(musical)


print("Jon Sina")
print("Jon Sina Arab")