import pandas as pd
import sklearn

df_collections = pd.read_csv('/home/giandbt/Documents/hack/team_garbage/data/2019-09-27-basel-collections.csv')
print(df_collections.columns)

df_measures = pd.read_csv('/home/giandbt/Documents/hack/team_garbage/data/2019-09-27-basel-measures_clean.csv')
del df_measures['Unnamed: 17']
print(df_measures.columns)

example = df_measures['osm_id'][0]
print(example)

df_collections = df_collections.fillna(0)
df_collections = df_collections.astype({'osm_id': 'int64'})
test = df_collections[df_collections["osm_id"] == int(example)]
print(test)
