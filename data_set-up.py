import pandas as pd
import numpy as np
from shapely.wkt import loads as load_wkt

def centroid(point):
    p1 = load_wkt(point)
    return p1.centroid.x, p1.centroid.y

# get colections
df_collections = pd.read_csv('/home/giandbt/Documents/hack/team_garbage/data/2019-09-27-basel-collections.csv')
df_collections = df_collections.fillna(0)
df_collections = df_collections.astype({'osm_id': 'int64'})

# get measures
df_measures = pd.read_csv('/home/giandbt/Documents/hack/team_garbage/data/2019-09-27-basel-measures.csv')
df_collections = df_collections.fillna(0)
df_collections = df_collections.astype({'osm_id': 'int64'})

days = []
months = []
years = []
times = []
ccis = []
place_types = []
longitudes = []
latitudes = []
geometry = []

place_type_list = df_measures.place_type.unique()
print(place_type_list)

df_measures['weekday'] = pd.to_datetime(df_measures['date']).dt.dayofweek
df_measures['day_type'] = (df_measures['weekday'] >= 5).astype(int)

for index, row in df_measures.iterrows():
    print(index)
    osm_id = row['osm_id']
    cci_id = row['cci_id']

    labels = df_collections[df_collections['osm_id'] == osm_id].index.values.tolist()
    num_matches = len(labels)
    if num_matches == 1:
        if df_collections['geometry'][labels[0]] == 'Polygon':
            geometry.append(0)
        else:
            geometry.append(1)
        coordinate = df_collections['coordinates'][labels[0]]
        longitude, latitude = centroid(coordinate)
        longitudes.append(longitude)
        latitudes.append(latitude)
    else:
        for label in labels:
            if df_collections['cci_id'][label] == cci_id:
                if df_collections['geometry'][label] == 'Polygon':
                    geometry.append(0)
                else:
                    geometry.append(1)
                coordinate = df_collections['coordinates'][label]
                longitude, latitude = centroid(coordinate)
                longitudes.append(longitude)
                latitudes.append(latitude)

    date, time = row['date'].split(' ')
    place_type = row['place_type']
    place_type = np.where(place_type_list == place_type)[0][0]
    place_types.append(place_type)

    year, month, day = date.split('-')

    if month == '04' and day == '22':
        df_measures.at[index, 'day_type'] = 2
    if month == '05' and day == '01':
        df_measures.at[index, 'day_type'] = 2
    if month == '05' and day == '30':
        df_measures.at[index, 'day_type'] = 2
    if month == '06' and day == '10':
        df_measures.at[index, 'day_type'] = 2
    if month == '08' and day == '01':
        df_measures.at[index, 'day_type'] = 2
    if month == '09' and day == '15':
        df_measures.at[index, 'day_type'] = 2

    days.append(day)
    months.append(int(month))
    years.append(int(year))
    times.append(time)

df_clean = df_measures.copy()
del df_clean['suitcase_id']
del df_clean['place_name']
del df_clean['rateCigarrettes']
del df_clean['rateBottles']
del df_clean['rateExcrements']
del df_clean['rateSyringues']
del df_clean['rateGums']
del df_clean['rateLeaves']
del df_clean['rateGrits']
del df_clean['rateGlassDebris']
del df_clean['place_type']
del df_clean['ratePapers']

df_clean['days'] = days
df_clean['months'] = months
df_clean['place_type'] = place_types
df_clean['geometry'] = geometry
df_clean['latitudes'] = latitudes
df_clean['longitudes'] = longitudes


df_clean.to_csv(r'./data/clean_datav2.csv')



