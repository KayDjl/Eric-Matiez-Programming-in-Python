import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename ='data/world_fires_7_day.csv'
with open(filename) as f:
    contecst_data = csv.reader(f)
    header = next(contecst_data)
    lati, long, frp = [], [], []
    for value in contecst_data:
        lat = float(value[0])
        lon = float(value[1])
        fr = float(value[3])
        lati.append(lat)
        long.append(lon)
        frp.append(fr)

    
data = [{
    'type': 'scattergeo',
    'lon': long,
    'lat': lati,
    'marker': {
        'color': frp,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'FRP'}
        },
    }]
my_layout = Layout(title='Global fires')
fig = {'data': data, 'layout': my_layout}
offline.plot(data, filename ='global_fires.html')
    
