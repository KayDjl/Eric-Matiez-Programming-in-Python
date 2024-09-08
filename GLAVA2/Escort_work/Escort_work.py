import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, gas, low = [], [], []   
    for i, v in enumerate(header_row):
        print(i, v)
    for vr in reader:
        ga = int(vr[1])
        year = datetime.strptime(vr[0], '%Y-%m-%d')
        lo = int(vr[2])
        dates.append(year)
        gas.append(ga)
        low.append(lo)
plt.style.use('seaborn-v0_8-dark')
fig, ax = plt.subplots()
ax.plot(dates, gas, c='red', alpha=0.5)
plt.plot(dates, low, c='blue', alpha=0.5)
plt.fill_between(dates, gas, low, facecolor='blue', alpha=0.1)
fig.autofmt_xdate()
ax.set_title('Temperatura', fontsize=24)
ax.set_xlabel('Date', fontsize=15)
ax.set_ylabel('TM Farengeyt', fontsize=15)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()

