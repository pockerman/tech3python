"""
Statistics Example 1:

Compute basic statistics using NumPy

"""

import numpy as np


def main():

    #create a dataset from the uniform distribution
    sample_1 = np.random.uniform(size=20)

    # calculate the mean
    mean_1 = np.mean(sample_1)

    # calculate the variance
    var_1 = np.var(sample_1)

    print("Mean: %f, variance %f "%(mean_1, var_1))

    # Let's take a second sample from the same distribution
    sample_2 = np.random.uniform(size=20)

    mean_1 = np.mean(sample_2)
    var_1 = np.var(sample_2)

    print("Mean: %f, variance %f "%(mean_1, var_1))

    # let's compute the covariance between the two samples
    # we will stack the two samples together
    mat = np.vstack((sample_1, sample_2))

    # compute the covariance matrix
    cov_mat = np.cov(mat)

    print(cov_mat)


if __name__ == '__main__':
    main()
