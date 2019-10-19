"""
Category: Numerics, Integration
ID: Example 2
Description: Calculate PI using Monte Carlo integration
Taken From the book: Kalman and Bayesian Filters in Python
Dependencies:

Details:

# TODO: Write details for Monte Carlo integration

"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import uniform


def f(x):
    return x*x


def main():

    N = 20000
    radius = 1

    area = (2*radius)**2
    pts = uniform(-1, 1, (N,2))

    # distance from center
    dist = np.linalg.norm(pts, axis=1)
    in_circle = dist <= 1
    pts_in_circle = np.count_nonzero(in_circle)
    pi = area * (pts_in_circle/N)

    print('mean pi(N={})= {:.4f}'.format(N, pi))
    print('err pi(N={})= {:.4f}'.format(N, np.pi - pi))

    # plot results
    plt.scatter(pts[in_circle,0], pts[in_circle,1], marker=',', edgecolor='k', s=1)
    plt.scatter(pts[~in_circle,0], pts[~in_circle,1], marker=',', edgecolor='r', s=1)
    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    print("Running Example numerics/example_2")
    main()
    print("Done...")