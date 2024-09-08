import matplotlib.pyplot as plt
from Die import Die

die = Die()
result = []

for roll in range(1000):
    rand = die.roll()
    result.append(rand)
    
apll = []

for value in range(1, die.check1+1):
    apl = result.count(value)
    apll.append(apl)
    

fig, ax = plt.subplots()

ax.set_title('One D6 for 1000 check', fontsize = 15)
ax.set_xlabel('Colv check', fontsize = 15)
ax.set_ylabel('Colv ppp', fontsize = 15)

ax.hist(result, bins=range(1, die.check1 + 2), edgecolor = 'black')

ax.set_xticks(range(1, die.check1 + 1))
plt.show()
