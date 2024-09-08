alien_0 ={'color': 'green', 'points': 5}
alien_1 ={'color': 'yellow', 'points': 10}
alien_2 ={'color': 'red', 'points': 15}
aliens =[alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

alienss = []

for aliens_number in range(30):
    new_alien = {'color': 'red', 'points': 15, 'speed': 'fast'}
    alienss.append(new_alien)

for alien1 in alienss[:5]:
    print(alien1)

print(f'{len(alienss)}')

for alien2 in alienss[0:3]:
    if alien['color'] =='red':
        alien2['color'] = 'yellow'
        alien2['points'] = 10
        alien2['speed'] = 'medium'

for alien in alienss[0:10]:
    print(alien)


users = {
    'lika228': {
        'ferst': 'lika',
        'last': 'yugova',
        'location': 'lermontov',
    },

    'sergey777': {
        'ferst': 'sergey',
        'last': 'polozkov',
        'location': 'pyatigorsk',
    },
}

for name, info_user in users.items():
    print(f'\nUsername: {name}')
    full_name = f"{info_user['ferst']} {info_user['last']}"
    location_user = f"{info_user['location']}"
    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location_user}")