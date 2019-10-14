"""
Category: Plotting
ID: Example 1
Description: Plot the binomial distribution
Taken From: https://www.astroml.org/book_figures/chapter3/fig_binomial_distribution.html

Details:


"""

import numpy as np
from scipy.stats import binom
from matplotlib import pyplot as plt


def main():
    # Define the distribution parameters to be plotted
    n_values = [20, 20, 40]
    b_values = [0.2, 0.6, 0.6]
    linestyles = ['-', '--', ':']
    x = np.arange(-1, 200)

    # plot the distributions
    fig, ax = plt.subplots(figsize=(5, 3.75))

    for (n, b, ls) in zip(n_values, b_values, linestyles):
        # create a binomial distribution
        dist = binom(n, b)

        plt.plot(x, dist.pmf(x), color='black', linestyle='steps-mid' + ls, label=r'$b=%.1f,\ n=%i$' % (b, n))

    plt.xlim(-0.5, 35)
    plt.ylim(0, 0.25)

    plt.xlabel('$x$')
    plt.ylabel(r'$p(x|b, n)$')
    plt.title('Binomial Distribution')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    print("Running Example plotting/example_2")
    main()
    print("Done...")