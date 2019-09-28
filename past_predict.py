import pandas as pd
import numpy as np
import dateutil

df = pd.read_csv('/home/giandbt/Documents/hack/team_garbage/data/clean_datav4.csv')

comb_ids = []
for index, row in df.iterrows():
    comb_id = str(row['osm_id']) + '_' + str(row['cci_id'])
    comb_ids.append(comb_id)

df['comb_ids'] = comb_ids
df.sort_values('comb_ids')
del df['Unnamed: 0']
df.to_csv(r'./data/clean_datav5.csv')