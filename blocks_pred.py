import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import dateutil
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt
from sklearn.utils.multiclass import unique_labels

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

df = pd.read_csv('/home/giandbt/Documents/hack/team_garbage/data/clean_datav5.csv')
df = df.sample(frac=1).reset_index(drop=True)
y_train = df['cci'].values
X_train = df['group_ids'].values

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train , train_size = 0.9, random_state =  90)
classes = np.unique(X_train)

predictions = {}
for id in classes:
    cci_sum = 0
    n = 0
    for idx, feature in enumerate(X_train):
        if feature == id:
            n += 1
            cci_sum += y_train[idx]
    predictions[id] = cci_sum/n

print(predictions)
del df['Unnamed: 0']

labels_classes = []
for label in y_val:
    if label < 3:
        labels_class = 0
    elif label >= 3 and label <=4:
        labels_class = 1
    else:
        labels_class = 2
    labels_classes.append(labels_class)
y_val = np.array(labels_classes)

size_val = len(X_val)

y_preds = []
for idx, feature in enumerate(X_val):
    try:
        y_pred = predictions[feature]
        if y_pred < 3:
            labels_class = 0
        elif y_pred >= 3 and y_pred <= 4:
            labels_class = 1
        else:
            labels_class = 2
        y_preds.append(labels_class)
    except:
        print(idx)
        y_preds.append(2)

'''
summation = 0
for i in range (0,size_val):  #looping through each element of the list
  difference = y_preds[i] - y_val[i]  #finding the difference between observed and predicted value
  squared_difference = difference**2  #taking square of the differene
  summation = summation + squared_difference  #taking a sum of all the differences
MSE = summation/size_val  #dividing summation by total values to obtain average
print("The Mean Square Error is: " , MSE)
'''
classes = np.unique(y_val)
plot_confusion_matrix(y_val, y_preds, classes)
plt.show()

#df.to_csv(r'./data/clean_datav6.csv')
