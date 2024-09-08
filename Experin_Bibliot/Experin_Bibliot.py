import plotly.graph_objs as go
from plotly import offline
from blyd import Blyd


bl = Blyd()
bl.fill_walk()

x_config = {'title': 'Result'}
y_config = {'title': 'Step numbers'}

my_layt = go.Layout(title='Random step', xaxis=x_config, yaxis=y_config)
scatter = go.Scatter(x=bl.x_values, y=bl.y_values, mode='markers')
fig = go.Figure(data=[scatter], layout=my_layt)
offline.plot(fig, filename='bled.html')


