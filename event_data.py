import pandas as pd
import numpy as np
import dateutil

df = pd.read_csv('/home/giandbt/Documents/hack/team_garbage/data/clean_datav3.csv')
df_events = pd.read_csv('/home/giandbt/Documents/hack/team_garbage/events/events_data.csv')
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
df['event'] = df.shape[0] * [0]

for index, row in df_events.iterrows():
    print(index)
    longitude = row['longitude']
    latitude = row['latitude']
    time = dateutil.parser.parse(row['start_time'])
    month = time.month
    day = time.day

    for idx, long in enumerate(longitudes):
        if longitude < longitudes[idx+1]:
            break
    for jdx, lat in enumerate(latitudes):
        if latitude < latitudes[jdx+1]:
            break

    group_id_event = str(idx) + str(jdx)
    past_days = 3
    df_affected = df.loc[(df['months'] <= int(month)) & (df['group_ids'] == int(group_id_event)) & (df['days'] >= day-past_days) & (df['days'] <= day)]
    for index, row in df_affected.iterrows():
        df['event'][index] = 1

df.to_csv(r'./data/clean_datav4.csv')