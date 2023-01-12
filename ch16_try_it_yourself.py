# 16-1. Sitka Rainfall: Sitka is in a temperate rainforest, so it gets a fair
# amount of rainfall. In the data file sitka_weather_2018_simple.csv is a
# header called PRCP, which represents daily rainfall amounts. Make a
# visualization focusing on the data in this column. You can repeat the
# exercise for Death Valley if you’re curi- ous how little rainfall occurs in a
# desert.
import csv
import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get dates, high, and low temperatures from this file.
    dates, precipitation = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        daily_precip = float(row[3])
        dates.append(current_date)
        precipitation.append(daily_precip)
        
#plot precipitation
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precipitation, c='red')

#format plot
ax.set_title('Daily precipitation - 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Precipitation (cm)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

# plt.show()
# 16-2. Sitka–Death Valley Comparison: The temperature scales on the Sitka and
# Death Valley graphs reflect the different data ranges. To accurately compare
# the temperature range in Sitka to that of Death Valley, you need identical
# scales on the y-axis. Change the settings for the y-axis on one or both of
# the charts in Figures 16-5 and 16-6. Then make a direct comparison between
# temperature ranges in Sitka and Death Valley (or any two places you want to
# compare).

# 16-3. San Francisco: Are temperatures in San Francisco more like temperatures
# in Sitka or temperatures in Death Valley? Download some data for San
# Francisco, and generate a high-low temperature plot for San Francisco to make
# a comparison.