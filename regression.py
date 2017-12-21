import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.utils import shuffle

# Load machine ready data
data = pd.read_csv('machine_library.csv')

# Randomly shuffle rows
data = shuffle(data)

# Determine training set portion
split_ratio = 0.8
split = int(data.shape[0] * split_ratio)

# Set training data and target data
X = np.array(data.loc[:, np.delete(data.columns.values,0)])
Y = np.array(data.loc[:, ['my_rating']]).ravel()

# Instantiate multiclass classification logistic regression model
logreg = linear_model.LogisticRegression(C=1e5)

# Fit model
logreg.fit(X[0:split],Y[0:split])

# Set hypothesis and true target data
h = logreg.predict(X[split:])
y = Y[split:]

# Print array results
print(y)
print(h)

# Define our custom error rate function, returns a result [0-1]. 1: perfect fit, 0: opposite fit
def error_rate(h, y):
    l = len(h)
    error = 0
    for i in range(l):
        error += (abs(y[i] - h[i])/4)

    return 1-error/l

# Print error rate with hypothesis and true target data
print(error_rate(h,y))

# Output:
# [4 5 3 4 2 4 4 4 5 5]
# [5 3 3 4 4 3 3 4 3 5]
#  0.775