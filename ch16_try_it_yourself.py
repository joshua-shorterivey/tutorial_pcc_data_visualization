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


# 16-6. Refactoring: The loop that pulls data from all_eq_dicts uses variables for the magnitude, longitude, latitude, and title of each earthquake before appending these values to their appropriate lists. This approach was chosen for clarity in how to pull data from a JSON file, but it’s not necessary in your code. Instead of using these temporary variables, pull each value from eq_dict and append it to the appropriate list in one line. Doing so should shorten the body of this loop to just four lines.
import json

#explore the structure of the data. 
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats= [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])

print(mags[:10])
print(lons[:5])
print(lats[:5])

# 16-7. Automated Title: In this section, we specified the title manually when defining my_layout, which means we have to remember to update the title every time the source file changes. Instead, you can use the title for the data set in the metadata part of the JSON file. Pull this value, assign it to a variable, and use this for the title of the map when you’re defining my_layout.
my_title = all_eq_data['metadata']['title']

# 16-8. Recent Earthquakes: You can find data files containing information about the most recent earthquakes over 1-hour, 1-day, 7-day, and 30-day periods online. Go to https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php and you’ll see a list of links to data sets for various time periods, focusing on earthquakes of different magnitudes. Download one of these data sets, and create a visualization of the most recent earthquake activity.
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data/jan_2023_all_month.geojson"
with open(filename) as f:
    jan_eq = json.load(f)
eq_dicts = jan_eq['features']
eq_dicts[0]

mags, lons, lats, hover_texts = [],[],[],[]
for eq in eq_dicts:
    mags.append(eq['properties']['mag'])
    lons.append(eq['geometry']['coordinates'][0])
    lats.append(eq['geometry']['coordinates'][1])
    hover_texts.append(eq['properties']['title'])
    
mags[6136] = 1
for idx,mag in enumerate(mags):
    if mag < 0 :
        print(idx,mag,mag*-1)
        
        

data=[{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats, 
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags, 
        'colorscale': 'Viridis', 
        'reversescale': True, 
        'colorbar': {'title': 'Magnitude'},
    } 
}]
my_layout = Layout(title='Jan Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='jan_global_earthquakes.html')

# 16-9. World Fires: In the resources for this chapter, you’ll find a file called world_fires_1_day.csv. This file contains information about fires burning in dif- ferent locations around the globe, including the latitude and longitude, and the brightness of each fire. Using the data processing work from the first part of this chapter and the mapping work from this section, make a map that shows which parts of the world are affected by fires.
# You can download more recent versions of this data at https://earthdata .nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/. You can find links to the data in CSV format in the TXT section.

filename = "data/world_fires_1_day.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    lats, lons, brights, hover_texts = [], [], [], []
    for row in reader:
        lats.append(row[0])
        lons.append(row[1])
        brights.append(float(row[2]))
        hover_texts.append(row[6])

data = [{
    'type': 'scattergeo',
    'lon': lons, 
    'lat': lats, 
    'text': hover_texts, 
    'marker': {
        'size': [brightness/30 for brightness in brights],
        'color': brights, 
        'colorscale': 'oranges', 
        'reversescale': True, 
        'colorbar': {'title': 'Brightness'},
    }
}]
my_layout = Layout(title='Day of Fires')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='1_day_fires.html')