from operator import itemgetter
import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

sub_cont = r.json()
sub_dick = []

for id_sub in sub_cont[:10]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{id_sub}.json'
    r = requests.get(url)
    print(f'Status code id: {r.status_code}')
    respons_r = r.json()
    try: 
        sub_dik = {
            'title': respons_r['title'],
            'hn_link': f'https://hacker-news.firebaseio.com/v0/item/id={id_sub}',
            'comments': respons_r['descendants'],
            }
    except KeyError:
        print("Error")
    sub_dick.append(sub_dik)
    
sub_dick = sorted(sub_dick, key=itemgetter('comments'))


for sub in sub_dick:
    print(f"\nTitle: {sub['title']}")
    print(f"Link: {sub['hn_link']}")
    print(f'Comments: {sub['comments']}')
