"""

Category: Statistics
ID: Example 5
Description: Simple Linear Regression with scikit-learn
Taken From: https://realpython.com/linear-regression-in-python/
Dependencies NumPy, scikit-learn
"""

import numpy as np
from sklearn.linear_model import LinearRegression


def main(*args, **kwargs):

    x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
    y = np.array([5, 20, 14, 32, 22, 38])

    # plot the data

    """
    Create the model:
    
    
    - fit_intercept is a Boolean (True by default) that decides whether to calculate the intercept 𝑏₀ (True) or consider it equal to zero (False).
    - normalize is a Boolean (False by default) that decides whether to normalize the input variables (True) or not (False).
    - copy_X is a Boolean (True by default) that decides whether to copy (True) or overwrite the input variables (False).
    - n_jobs is an integer or None (default) and represents the number of jobs used in parallel computation. None usually means one job and -1 to use all processors.

    """
    model = LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None)
    model.fit(x, y)

    print('intercept:', model.intercept_)
    print('slope:', model.coef_)
    print('coefficient of determination:', model.score(x, y))


if __name__ == '__name__':

    print("Running Example statistics/example_5")
    main()
    print("Done...")