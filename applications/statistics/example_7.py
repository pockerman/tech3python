"""
Category: Statistics
ID: Example 7
Description: Almost sure convergence
Taken From: Python for Probability, Statistics and Machine Learning
Dependencies: Numpy, scipy
"""
import random
from scipy import stats
import numpy as np
from plot.two_d_plotter import TwoDPlotter

def main():

    # get an instance of the uniform distribution
    u = stats.uniform()

    NUM_ITRS = 1000
    SAMPLE_SIZE = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    x = []
    y = []

    for itr in range(NUM_ITRS):
        sample_size = random.choice(SAMPLE_SIZE)
        sample = u.rvs(sample_size)
        xn = sample.max()
        x.append(sample_size)
        y.append(xn)

    kwargs={'plot_title': " Max $X_n$ vs Sample size $n$", 'xlabel': "$n", 'ylabel': '$max{X_1,X_2,...X_n}$'}
    plotter = TwoDPlotter(kwargs=kwargs)
    plotter.plot(x=x, y=y)
    #plotter.show_plots()

    mean = np.mean([u.rvs(60).max() > 0.95 for i in range(1000)])
    print(mean)

    # plug in epsilon and the desired probability constraint



if __name__ == '__main__':
    print("Running Example statistics/example_7")
    main()
    print("Done...")