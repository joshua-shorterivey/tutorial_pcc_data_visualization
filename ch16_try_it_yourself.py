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
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # get dates, high, and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get dates, high, and low temperatures from this file.
    dv_highs, dv_lows = [], []
    for row in reader:
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dv_highs.append(high)
            dv_lows.append(low)


#plot temps for sitka
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', label='sitka high')
ax.plot(dates, lows, c='blue', label='sitka low')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#plot temps for death_valley
ax.plot(dates, dv_highs, c='pink', label='death valley high')
ax.plot(dates, dv_lows, c='green', label='death valley low')
ax.fill_between(dates, dv_highs, dv_lows, facecolor='green', alpha=0.1)

#format plot
ax.set_title('Daily high and low temperatures - 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.legend()
fig.autofmt_xdate()
ax.set_ylabel('Temperatures (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# 16-3. San Francisco: Are temperatures in San Francisco more like temperatures
# in Sitka or temperatures in Death Valley? Download some data for San
# Francisco, and generate a high-low temperature plot for San Francisco to make
# a comparison.
filename = 'data/sf_weather_2022.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get dates, high, and low temperatures from this file.
    dates, sf_highs, sf_lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            sf_highs.append(high)
            sf_lows.append(low)


#plot temps for sitka
plt.style.use('seaborn')
fig, ax = plt.subplots()

#plot temps for death_valley
ax.plot(dates, sf_highs, c='pink', label='high')
ax.plot(dates, sf_lows, c='green', label='low')
ax.fill_between(dates, sf_highs, sf_lows, facecolor='green', alpha=0.1)

#format plot
ax.set_title('Daily high and low temperatures - 2022', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.legend()
fig.autofmt_xdate()
ax.set_ylabel('Temperatures (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# 16-4. Automatic Indexes: In this section, we hardcoded the indexes
# corresponding to the TMIN and TMAX columns. Use the header row to determine
# the indexes for these values, so your program can work for Sitka or Death
# Valley. Use the station name to automatically generate an appropriate title
# for your graph as well.

# 16-5. Explore: Generate a few more visualizations that examine any other
# weather aspect you’re interested in for any locations you’re curious about.