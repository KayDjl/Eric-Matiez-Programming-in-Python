import matplotlib.pyplot as plt

input_values = list(range(1, 1001))
squares = [x**2 for x in input_values]
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(input_values, squares, c=input_values, cmap=plt.cm.Reds, s=10)
ax.set_ylim([0, 1009000])
ax.set_xlim([0, 1100])

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()
