
"""
Category: Statistics
ID: Example 2
Description: Compute the mean, standard deviation and correlation of two variables
"""

import numpy as np


def main():

    weights = np.array([ 4.4, 5.3, 7.2, 5.2, 8.5,  7.3, 6.0, 10.4, 10.2, 6.1])
    age = np.array([1, 3, 5, 2, 11,  9, 3, 9, 12, 3 ])

    # compute the means
    mu_w = np.mean(weights)
    sd_w = np.std(weights)
    print("Mean weights: %f std weights %f "%(mu_w, sd_w))
    mu_age = np.mean(age)
    sd_age = np.std(age)
    print("Mean age: %f std age %f "%(mu_age, sd_age))

    R = np.corrcoef(x=weights, y= age)
    print(R)

    # since we want the correlation between Weight and Age
    # get the off diagonal component
    print("Correlation coefficient %f "%R[0][1])


if __name__ == '__main__':
    main()