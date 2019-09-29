import pandas as pd
import numpy as np
import os
import collections
from sklearn import datasets, preprocessing
from sklearn.utils import class_weight
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from keras.models import Sequential, Model, load_model
from keras.layers import Input, Dense, Dropout
from keras.callbacks import ModelCheckpoint
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
from sklearn.model_selection import StratifiedShuffleSplit
from imblearn.under_sampling import RandomUnderSampler

def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax

df = pd.read_csv('./data/clean_datav4.csv')
df = df.sample(frac=1).reset_index(drop=True)

y_train = df['cci'].values
labels_classes = []
for label in y_train:
    if label < 3:
        labels_class = 0
    elif label >= 3 and label <=4:
        labels_class = 1
    else:
        labels_class = 2
    labels_classes.append(labels_class)
y_train = np.array(labels_classes)

X_train = df[['cci']]

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# Hyper-parameters
SEED = 7
EPOCHS = 19
BATCH_SIZE= 32

# Check if the dataset is imbalanced and correct if necessary
counter = collections.Counter(y_train)
print(X_train.shape,y_train.shape, counter)

# fix random seed for reproducibility
np.random.seed(SEED)

# Regularize Dataset
scaler = preprocessing.StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)

rus = RandomUnderSampler(return_indices=True)
X_train, y_train, id_rus = rus.fit_sample(X_train, y_train)


class_weights = class_weight.compute_class_weight('balanced', np.unique(y_train), y_train)
print(class_weight)
# Divide dataset into training and validation (maintaining the distribution as before)
sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=0)
for train_index, test_index in sss.split(X_train, y_train):
    X_train, X_val = X_train[train_index], X_train[test_index]
    y_train, y_val = y_train[train_index], y_train[test_index]

counter = collections.Counter(y_train)
print(X_train.shape,y_train.shape, counter)

# Multi-class Neural Network
clf = Sequential()
clf.add(Dense(X_train.shape[1], activation='relu'))
clf.add(Dense(10, activation='relu'))
clf.add(Dropout(0.3))
clf.add(Dense(3))
clf.compile(optimizer='adam', loss='sparse_categorical_crossentropy',  metrics=['acc'])

mcp_save = ModelCheckpoint('classifier.hdf5', save_best_only=True, monitor='val_loss', mode='min')
history = clf.fit(X_train, y_train, verbose=2, epochs=EPOCHS, batch_size=BATCH_SIZE, callbacks=[mcp_save], validation_data=(X_val, y_val),class_weight=class_weights)

# plot history
plt.plot(history.history['acc'], label='train')
plt.plot(history.history['val_acc'], label='test')
plt.legend()
plt.show()

y_pred_prob = clf.predict(X_val)
y_pred = []
for i in range(1,y_pred_prob.shape[0]+1):
    y_pred.append((np.argmax(y_pred_prob[i-1])))


#Plot Confusius Matrix
classes = np.unique(y_val)
print(classes)

plot_confusion_matrix(y_val, y_pred, classes)
plt.show()