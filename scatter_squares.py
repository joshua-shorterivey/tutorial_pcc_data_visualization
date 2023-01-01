import matplotlib.pyplot as plt


#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]

#calculating data automatically
x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# c for color -> can use rgb values as well
#ax.scatter (x_values, y_values, c='red', s=10)
#ax.scatter (x_values, y_values, c=(0, 0.8, 0), s=10)

# assigning color based on y_value and color map
ax.scatter (x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set chart title and label axes;
ax.set_title("square numbers", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel('square of value', fontsize=14)

# set size of tick lables.
ax.tick_params(axis='both', which='major', labelsize=14)

# set the range for each axis. 
ax.axis([0, 1_100, 0, 1_100_000])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
