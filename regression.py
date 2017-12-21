import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.utils import shuffle

# Load machine ready data
data = pd.read_csv('machine_library.csv')

iterations = 100

# Define our custom error rate function, returns a result [0-1]. 1: perfect fit, 0: opposite fit
def error_rate(h, y):
    l = len(h)
    error = 0
    for i in range(l):
        error += (abs(y[i] - h[i])/4)

    return 1-error/l

# Define our modeling function. Parameter j sets the training/testing data ratio.
# Returns (hypothesis target data, true target data, error rate) tuple
def fit(j):
    # Determine training set portion
    split = int(data.shape[0] * j)

    # Set training data and target data
    X = np.array(data.loc[:, np.delete(data.columns.values, 0)])
    Y = np.array(data.loc[:, ['my_rating']]).ravel()

    # Instantiate multiclass classification logistic regression model
    logreg = linear_model.LogisticRegression(C=1e5)

    # Fit model
    logreg.fit(X[0:split], Y[0:split])

    # Set hypothesis and true target data
    h = logreg.predict(X[split:])
    y = Y[split:]

    return (h,y,error_rate(h,y))

# Define our results DataFrame, organized by j value, which dictates split ratio
# Designed to maximize training data for this small data set
results = pd.DataFrame(columns=[str(a) for a in range(4,19)], index=[0])

for _ in range(iterations):
    # Randomly shuffle rows
    data = shuffle(data)

    for j in range(4, 19):
        # Append error rate, of hypothesis and true target data, to j column in results DF
        results = results.append({str(j): fit(j/20)[2]}, ignore_index=True)

f = fit(.75)
print(f[0])
print(f[1])
print(f[2])

results.plot.box()

plt.show()