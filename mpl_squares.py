import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
sqaures = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# adjusting for legibility --> linewidth
ax.plot(input_values, sqaures, linewidth=3)

#set chart title and lable axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set size of tick labels
ax.tick_params(axis='both', labelsize=14)
plt.show()