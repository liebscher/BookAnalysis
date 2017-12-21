import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.utils import shuffle

# Load machine ready data
data = pd.read_csv('machine_library.csv')

# Total iterations of fitting
iterations = 250

# Total increments of j
increments = 25

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


# Range of increments to use. Must cut of low end and high end to ensure valid training/testing portions
rng = (int(increments*0.2), int(increments*0.9))

# Define our results DataFrame, organized by j value, which dictates split ratio
# Designed to maximize training data for this small data set
results = pd.DataFrame(columns=[str(a/increments) for a in range(rng[0], rng[1])], index=[0])

for _ in range(iterations):
    # Randomly shuffle rows
    data = shuffle(data)

    for j in range(rng[0], rng[1]):
        # Append error rate, of hypothesis and true target data, to j column in results DF
        results = results.append({str(j/increments): fit(j/increments)[2]}, ignore_index=True)

# Sample
f = fit(.78)
print(f[0])
print(f[1])
print(f[2])

# [5 3 2 4 4 4 4 5 2 5 5]
# [3 3 4 4 3 4 3 5 2 5 5]
# 0.863636363636

results.plot.box(title='Effect of training data ratio on Error Rate')

plt.show()