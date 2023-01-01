"""module to hold chapter 15 try it yourself exercises"""
# 15-1. Cubes: A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5000 cubic numbers.
import matplotlib.pyplot as plt

# Plotting first 5 cubic numbers
x_values = range(1, 6)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.plot(x_values, y_values)

#set chart title and lable axes
ax.set_title('Cube Numbers', fontsize=12)
ax.set_xlabel('Value')
ax.set_ylabel('Cube of Value')

#show visual
ax.tick_params(axis='x')
plt.show()

### ---- ###

#plotting first 5000 cubic numbers
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.plot(x_values, y_values)

#set chart title and lable axes
ax.set_title('Cube Numbers', fontsize=12)
ax.set_xlabel('Value')
ax.set_ylabel('Cube of Value')

#show visual
ax.tick_params(axis='x')
plt.show()


# 15-2. Colored Cubes: Apply a colormap to your cubes plot.
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap='cool', s=1)

#set chart title and lable axes
ax.set_title('Cube Numbers', fontsize=12)
ax.set_xlabel('Value')
ax.set_ylabel('Cube of Value')

#show visual
ax.tick_params(axis='x')
plt.show()