"""
Statistics Example 3
Illustration of basic bootstrap method for the mean
see also: https://machinelearningmastery.com/a-gentle-introduction-to-the-bootstrap-method/
"""

import numpy as np
from sklearn.utils import resample
import matplotlib.pyplot as plt

# the size of the sample
SIZE = 100

# how many bootstrap iterations to perform
ITERATIONS = 100

mu = 0.8
sigma = 0.1

def main():

    # draw a sample from the normal distribution
    dataset = np.random.normal(mu, sigma, SIZE)

    x_bar = np.mean(dataset)
    var = np.var(dataset)
    mean_variance = var / float(SIZE)

    print(f"Mean is: {x_bar} Variance is: {var}")
    print(f"Mean variance is : {mean_variance}")

    means = [0.0 for i in range(ITERATIONS)]

    for itr in range(ITERATIONS):
        sample = resample(dataset, replace=True, n_samples=10, random_state=1)
        means[itr] = np.mean(sample)

    mean_of_means = np.mean(means)
    print(f"Mean of means is: {mean_of_means}")

    # Let's make a plot of the empirical distribution of the means

    n_groups = 10

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.45
    opacity = 0.8

    rects1 = plt.bar(index, means, bar_width, alpha=opacity, color='b', label='Frank')

    plt.xlabel('Bin')
    plt.ylabel('Mean')
    plt.title('Means Distribution')
    # plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()