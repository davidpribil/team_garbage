import pandas as pd
import numpy as np
import shapefile as shp
import math
from shapely.wkt import loads as load_wkt

df = pd.read_csv('/home/giandbt/Documents/hack/team_garbage/data/clean_datav2.csv')
longitudes = df['longitudes'].values
latitudes = df['latitudes'].values

min_long = np.min(longitudes)
max_long = np.max(longitudes)
min_lat = np.min(latitudes)
max_lat = np.max(latitudes)
num_tiles = 10

dx = (max_long - min_long)/num_tiles
dy = (max_lat - min_lat)/num_tiles

longitudes = np.arange(min_long, max_long+dx, dx)
latitudes = np.arange(min_lat, max_lat+dx, dy)

group_ids = []

for index, row in df.iterrows():
    print(index)
    longitude = row['longitudes']
    latitude = row['latitudes']

    for idx, long in enumerate(longitudes):
        if longitude < longitudes[idx+1]:
            break
    for jdx, lat in enumerate(latitudes):
        if latitude < latitudes[jdx+1]:
            break

    group_id = str(idx) + str(jdx)
    group_ids.append(group_id)

df['group_ids'] = group_ids
df.to_csv(r'./data/clean_datav3.csv')