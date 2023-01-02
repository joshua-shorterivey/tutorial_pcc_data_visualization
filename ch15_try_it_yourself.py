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
