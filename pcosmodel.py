import pandas as pd
import numpy as np


df = pd.read_csv("data_use.csv")

y = df.iloc[:, 0]
X = df.iloc[:, 1:]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=9, metric='manhattan').fit(X_train, y_train)

import pickle
filename = 'savedmodel.sav'
pickle.dump(model, open(filename, 'wb'))
