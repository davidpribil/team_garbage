import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Input, Dense, Dropout
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

df = pd.read_csv('./data/clean_data.csv')

labels = df['cci'].values
features = df[['osm_id','Weekday', 'day_type', 'days', 'months', 'place_type', 'geometry' ]].values

# Hyper-parameters
SEED = 7
EPOCHS = 5
BATCH_SIZE = 16

# fix random seed for reproducibility
np.random.seed(SEED)

# Multi-class Neural Network
def build_model():
    clf = Sequential()
    clf.add(Dense(features.shape[1], activation='relu'))
    clf.add(Dense(5, activation='relu'))
    clf.add(Dropout(0.3))
    clf.add(Dense(3, activation='relu'))
    clf.add(Dropout(0.3))
    clf.add(Dense(1, kernel_initializer='normal'))
    clf.compile(optimizer='adam', loss='mean_squared_error')
    return clf

# evaluate model with standardized dataset
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=build_model, epochs=EPOCHS, batch_size=BATCH_SIZE, verbose=1)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10)
results = cross_val_score(pipeline, features, labels, cv=kfold)
print("Standardized: %.2f (%.2f) MSE" % (results.mean(), results.std()))
