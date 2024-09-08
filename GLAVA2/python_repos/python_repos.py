import requests
import json
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code:{r.status_code}")

response_dict = r.json()
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
repo_name, stars, description = [], [], []
for repo_dict in repo_dicts:
    url = repo_dict['html_url']
    name = repo_dict['name']
    link = f"<a href='{url}'>{name}</a>"
    repo_name.append(link)
    stars.append(repo_dict['stargazers_count'])
    onwer = repo_dict['owner']['login']
    descrip = repo_dict['description']
    label = f"{onwer}<br />{descrip}"
    description.append(label)
    
data = [{
    'type': 'bar',
    'x': repo_name,
    'y': stars,
    'hovertext': description,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
        },
    'opacity': 0.6,    
    }]

my_layout = {
    'title': 'Population progect',
    'titlefont': {'size': 38},
    'xaxis': {
        'title': 'Name developer',
        'titlefont': {'size': 34},
        'tickfont': {'size': 35},
        },
    'yaxis': {
        'title': 'Count stars',
        'titlefont': {'size': 34},
        'tickfont': {'size': 35}
        },
    'hoverlabel': {
        'font': {'size': 40},  
        },
    }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_dev.html')

for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repositories: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")
    
