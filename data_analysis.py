import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('./data/clean_data.csv')
zones = df[['osm_id', 'cci', 'months', 'days']]
fig, ax = plt.subplots(figsize=(15,7))
zones = zones.groupby(['osm_id', 'months', 'days']).mean()
print(zones)
results = zones.groupby(['osm_id']).var().values

'''
Monday = df.loc[(df['Weekday'] == 0)]
cci_mon = np.mean(Monday['cci'].values)
avg_ccis.append(cci_mon)
Tuesday = df.loc[(df['Weekday'] == 1)]
cci_tue = np.mean(Tuesday['cci'].values)
avg_ccis.append(cci_tue)
Wednesday = df.loc[(df['Weekday'] == 2)]
cci_wed = np.mean(Wednesday['cci'].values)
avg_ccis.append(cci_wed)
Thursday = df.loc[(df['Weekday'] == 3)]
cci_thu = np.mean(Thursday['cci'].values)
avg_ccis.append(cci_thu)
Friday = df.loc[(df['Weekday'] == 4)]
cci_fri = np.mean(Friday['cci'].values)
avg_ccis.append(cci_fri)
Saturday = df.loc[(df['Weekday'] == 5)]
cci_sat = np.mean(Saturday['cci'].values)
avg_ccis.append(cci_sat)
Sunday = df.loc[(df['Weekday'] == 6)]
cci_sun = np.mean(Sunday['cci'].values)
avg_ccis.append(cci_sun)

plt.plot(avg_ccis)
plt.show()
'''
