import pandas as pd
import numpy as np
import os
from sklearn import datasets, preprocessing
from sklearn.utils import class_weight
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from keras.models import Sequential, Model, load_model
from keras.layers import Input, Dense, Dropout
from keras.callbacks import ModelCheckpoint
import seaborn as sns

df = pd.read_csv('./data/clean_datav4.csv')
y_train = df['cci'].values

#X_train = df[['osm_id','weekday', 'day_type', 'place_type', 'latitudes', 'longitudes', 'group_ids', 'event',
#               'mean_temp', 'mean_wind_speed', 'total_prep']].values

X_train = df[['latitudes', 'longitudes']].values

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# Hyper-parameters
SEED = 7
EPOCHS = 19
BATCH_SIZE= 32

# fix random seed for reproducibility
np.random.seed(SEED)

# Regularize Dataset
scaler = preprocessing.StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)

# Divide dataset into training and validation (maintaining the distribution as before)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train , train_size = 0.9, random_state =  90)


# Multi-class Neural Network
clf = Sequential()
clf.add(Dense(X_train.shape[1], activation='relu'))
clf.add(Dense(1))
clf.compile(optimizer='adam', loss='mean_absolute_error',  metrics=['mse', 'mae'])

mcp_save = ModelCheckpoint('regressor.hdf5', save_best_only=True, monitor='val_loss', mode='min')

history = clf.fit(X_train, y_train, verbose=2, epochs=EPOCHS, batch_size=BATCH_SIZE, callbacks=[mcp_save], validation_data=(X_val, y_val))

# plot history
plt.plot(history.history['mse'], label='train_mse')
plt.plot(history.history['mae'], label='train_mae')
plt.plot(history.history['val_mse'], label='test')
plt.legend()
plt.show()

y_pred_prob = clf.predict(X_train)
print(y_pred_prob)


def correlation_heatmap(train):
    correlations = train.corr()

    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(correlations, vmax=1.0, center=0, fmt='.2f',
                square=True, linewidths=.5, annot=True, cbar_kws={"shrink": .70})
    #plt.show()
    plt.savefig('final_model_correlation.png', bbox_inches='tight')


X_train = df[['osm_id','weekday', 'day_type', 'place_type', 'latitudes', 'longitudes', 'group_ids', 'event',
               'mean_temp', 'mean_wind_speed', 'total_prep', 'cci']]

correlation_heatmap(X_train)