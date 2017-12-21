import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv('machine_library.csv')

data = shuffle(data)

split_ratio = 0.8
split = int(data.shape[0] * split_ratio)

X = np.array(data.loc[:, np.delete(data.columns.values,0)])
Y = np.array(data.loc[:, ['my_rating']]).ravel()

logreg = linear_model.LogisticRegression(C=1e5)


logreg.fit(X[0:split],Y[0:split])

print(Y[split:])
print(logreg.predict(X[split:]))