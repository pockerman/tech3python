"""
Category: Statistics
ID: Example 8
Description: Simulate the standard error for the mean is 1/sqrt(n)
Taken From:
Dependencies:
"""
import random
from scipy import stats
import numpy as np


def main():

    N_SIM = 1000
    n = 10
    mu = 0.0
    sigma = 1.0
    mean = []

    for itr in range(N_SIM):
        sample = np.random.normal(loc=mu, scale=sigma, size=n)
        mean.append(np.mean(sample))

    std = np.std(mean)
    print("Standard deviation  of means is: {}".format(std))
    print("1/sqrt(n) is: {} ".format(1/np.sqrt(n)))


if __name__ == '__main__':
    print("Running Example statistics/example_8")
    main()
    print("Done...")