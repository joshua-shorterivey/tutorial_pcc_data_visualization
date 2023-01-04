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

# 15-3. Molecular Motion: Modify rw_visual.py by replacing ax.scatter() with ax.plot(). To simulate the path of a pollen grain on the surface of a drop of water, pass in the rw.x_values and rw.y_values, and include a linewidth argu- ment. Use 5000 instead of 50,000 points.
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# keep making new walks, as long as the program is active.
while True:
    #make a random walk
    rw = RandomWalk()
    #increasing number of points
    #rw = RandomWalk(50_000)
    rw.fill_walk()

    #plot the points in the walk. 
    plt.style.use('classic')
    #altering size to fill screen with figsize
    fig, ax = plt.subplots(figsize=(10,6), dpi=227)

    #plotting with color to show path taken
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, c='blue', linewidth=1)

    #emphasize the first and last points.
    ax.scatter(0,0, c='green', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', 
        s=50)

    #remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()


    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break

# 15-4. Modified Random Walks: In the RandomWalk class, x_step and y_step are generated from the same set of conditions. The direction is chosen randomly from the list [1, -1] and the distance from the list [0, 1, 2, 3, 4]. Modify the values in these lists to see what happens to the overall shape of your walks. Try a longer list of choices for the distance, such as 0 through 8, or remove the −1 from the x or y direction list.

#makes the walks wider. more clumpy

# 15-5. Refactoring: The fill_walk() method is lengthy. Create a new method called get_step() to determine the direction and distance for each step, and then calculate the step. You should end up with two calls to get_step() in fill_walk():
#                   x_step = self.get_step()
#                   y_step = self.get_step()
# This refactoring should reduce the size of fill_walk() and make the method easier to read and understand.
from random import choice

class RandomWalk:
    """a class to generate random walks."""

    def __init__(self, num_points=5000) -> None:
        """initialize attributes of a walk."""
        #default 5_000 to generate interesting but quick processing routes
        self.num_points = num_points

        #all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """gathers step direction and distance"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """calculate all the points in a the walk"""

        # keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            #decide which direction to go and how far to go in that direction. 
            x_step = self.get_step()
            y_step = self.get_step()

            #reject moves that go nowhere. 
            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

# 15-6. Two D8s: Create a simulation showing what happens when you roll two eight-sided dice 1000 times. Try to picture what you think the visualization will look like before you run the simulation; then see if your intuition was correct. Gradually increase the number of rolls until you start to see the limits of your system’s capabilities.
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die(8)
die_2 = Die(8)
rolls = []

for i in range(1000):
    total = die_1.roll() + die_2.roll()
    rolls.append(total)

max_roll = die_1.num_sides + die_2.num_sides
frequencies = []

for num in range(2, max_roll+1):
    frequency = rolls.count(num)
    frequencies.append(frequency)

#visualize the results
x_values = list(range(2, max_roll+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 dice 1000 times', 
            xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')

# 15-7. Three Dice: When you roll three D6 dice, the smallest number you can roll is 3 and the largest number is 18. Create a visualization that shows what hap- pens when you roll three D6 dice.

die_1 = Die()
die_2 = Die()
die_3 = Die()
rolls = []

for i in range(1000):
    total = die_1.roll() + die_2.roll() + die_3.roll()
    rolls.append(total)

max_roll = die_1.num_sides * 3
frequencies = []

for num in range(2, max_roll+1):
    frequency = rolls.count(num)
    frequencies.append(frequency)

#visualize the results
x_values = list(range(1, max_roll+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 dice 1000 times', 
            xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6x3.html')

# 15-8. Multiplication: When you roll two dice, you usually add the two numbers together to get the result. Create a visualization that shows what happens if you multiply these numbers instead.
die_1 = Die()
die_2 = Die()
rolls = []

for i in range(1000):
    total = die_1.roll() * die_2.roll()
    rolls.append(total)

max_roll = die_1.num_sides * die_2.num_sides
frequencies = []

for num in range(1, max_roll+1):
    frequency = rolls.count(num)
    frequencies.append(frequency)

#visualize the results
x_values = list(range(1, max_roll+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 dice 1000 times', 
            xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')

# 15-9. Die Comprehensions: For clarity, the listings in this section use the long form of for loops. If you’re comfortable using list comprehensions, try writing a comprehension for one or both of the loops in each of these programs.

# 15-10. Practicing with Both Libraries: Try using Matplotlib to make a die-rolling visualization, and use Plotly to make the visualization for a random walk. (You’ll need to consult the documentation for each library to complete this exercise.)
