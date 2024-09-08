import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_1_day_m1.geojson'
filename1 = 'data/eq_data_30_day_m1.geojson'
with open(filename1, encoding='utf-8') as f:
    all_eq_date = json.load(f)

all_eq_dicts = all_eq_date['features']
mags, lons, lats, tit = [], [], [], []

all_title = all_eq_date['metadata'] ['title']

for magnet in all_eq_dicts:
    perm = (magnet['properties'] ['mag'], 
    magnet['geometry'] ['coordinates'] [0], 
    magnet['geometry'] ['coordinates'] [1], 
    magnet['properties'] ['title'])   
    mags.append(perm[0])
    lons.append(perm[1])
    lats.append(perm[2])
    tit.append(perm[3])

    
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': tit,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]
my_layout = Layout(title=all_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earth')

