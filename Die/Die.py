from roll import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

cub = Die()
cub2 = Die()
cub3 = Die()
result = []

for values in range(1000):
    roll_num = cub.roll() + cub2.roll() + cub3.roll()
    result.append(roll_num)
    
counts = []
max_result = cub.num_check + cub2.num_check + cub3.num_check
for val in range(3, max_result+1):
    fr = result.count(val)
    counts.append(fr)
    
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=counts)]

x_layout = {'title': 'Result', 'dtick': 1}
y_layout = {"title": 'Frequency of Result'}

my_layout = Layout(title='Result of rolling three D6 1000 times', xaxis=x_layout, yaxis=y_layout)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6AP.html')