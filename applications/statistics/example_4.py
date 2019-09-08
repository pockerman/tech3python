"""
Statistics Example 4

Illustration of basic bootstrap method for the skewness
For data coming from the normal distribution the skweness should be zero
see also: https://machinelearningmastery.com/a-gentle-introduction-to-the-bootstrap-method/
"""

import numpy as np
from sklearn.utils import resample
from scipy.stats import skew

# the size of the sample
SIZE = 100

# how many bootstrap iterations to perform
ITERATIONS = 100

mu = 0.8
sigma = 0.1

def main():

    # draw a sample from the normal distribution
    dataset = np.random.normal(mu, sigma, SIZE)

    # compute basic statistics from the dataset
    skewness = skew(dataset)
    x_bar = np.mean(dataset)
    var = np.var(dataset)
    mean_variance = var / float(SIZE)

    print(f"Mean is: {x_bar} Variance is: {var}")
    print(f"Skewness is: {skewness}")
    print(f"Mean variance is : {mean_variance}")

    skewnesses = [0.0 for i in range(ITERATIONS)]

    for itr in range(ITERATIONS):
        sample = resample(dataset, replace=True, n_samples=20, random_state=1)
        skewnesses[itr] = skew(sample)

    mean_of_skewnesses = np.mean(skewnesses)
    print(f"Mean of skewnesses is: {mean_of_skewnesses}")


if __name__ == '__main__':
    main()

