import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import figure
from matplotlib.pyplot import xticks, grid
from sklearn import linear_model
from sklearn.model_selection._split import train_test_split

# Labeled columns
headers = ('five_star', 'european', 'north_american', 'asian', 'other', 'author_gender', 'avg_rating', 'pages',
           'org_publication_year', 'duration', 'favorite', 'fiction', 'nonfiction', 'contemporary',
           'philosphy', 'politics', 'religion', 'science_tech_math', 'short_story', 'memoir', 'war_story', 'historical')

# Load machine ready data
data = pd.read_csv('machine_library.csv')

# Define our custom error rate function, returns a result [0-1]. 1: perfect fit, 0: opposite fit
def error_rate(h, y):
    l = len(h)
    error = 0
    for i in range(l):
        error += (abs(y[i] - h[i]) / 2)

    return 1 - error / l


# Define our modeling function. Parameter j sets the training/testing data ratio.
# Returns (hypothesis target data, true target data, error rate) tuple
def fit(j, testing=None, coef=False):
    # Set training data and target data
    X = np.array(data.loc[1:, np.delete(data.columns.values, 0)])
    Y = np.array(data.loc[1:, ['five_star']]).ravel()

    # Assign the training/testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1 - j)

    # Assign the testing set to the new vars if necessary
    if testing is None:
        testing = [X_test, Y_test]

    # Instantiate binary classification logistic regression model
    logreg = linear_model.LogisticRegression(C=1e5)

    # Fit model
    logreg.fit(X_train, Y_train)

    # Set hypothesis and true target data
    h = logreg.predict(testing[0])
    y = testing[1]

    # Return the coefficient matrix if necessary
    if coef:
        return (h, y, error_rate(h, y), logreg.coef_)

    return (h, y, error_rate(h, y))


# Use the first line of the data csv for single book testing
x = np.array(data.loc[0, np.delete(data.columns.values, 0)])

# Fit and predict with the new model
f = fit(.76, testing=[[x],[1]], coef=True)
#print((f[0],f[1],f[2]))

# Plot coefficient matrix
weights = pd.DataFrame(np.array(f[3]).transpose(), columns=['5 star'])
plt.figure(num=1, figsize=(14,10))
weights.plot.bar()
grid(True, alpha=0.4)
xticks(range(len(headers[1:])), headers[1:], rotation=30)

plt.show()
