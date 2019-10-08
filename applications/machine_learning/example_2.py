"""
Category: Machine Learning
ID: Example 2
Description: Simple Linear Regression
Taken From: Code from the book Python Data Science Handbook
https://jakevdp.github.io/PythonDataScienceHandbook/

Details:

//TODO: Fill in the details
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


def main():

    n_rnumbers = np.random.RandomState(42)
    x = 10 * n_rnumbers.rand(50)
    y = 2*x -1 + n_rnumbers.rand(50)

    plt.scatter(x, y)


    # arrang x as 50x1
    X = x[:, np.newaxis]

    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)

    print("Model intercept: ", model.intercept_)
    print("Model coefficients: ", model.coef_)


    xfit = np.linspace(-1, 11)
    Xfit = xfit[:, np.newaxis]
    yfit = model.predict(Xfit)

    plt.plot(xfit, yfit)
    plt.show()


if __name__ == '__main__':
    print("Running Example machine_learning/example_2")
    main()
    print("Done...")