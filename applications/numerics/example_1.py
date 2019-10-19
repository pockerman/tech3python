"""
Category: Numerics, Integration
ID: Example 1
Description: Monte Carlo integration
Taken From the book: Numerical C
Dependencies:

Details:

# TODO: Write details for Monte Carlo integration

"""

import random


def f(x):
    return x*x


def main():

    N_ITERATIONS = 100000
    a = 1.0
    b = 3.0

    total_area = 0.0
    area_under_curve = 0.0
    y_lower = 0.0
    y_upper = f(b)

    REAL_AREA = (b-a)*(f(b) - 0.0)

    for itr in range(N_ITERATIONS):
        # generate random x and y points
        x = random.uniform(a, b)
        y = random.uniform(0.0, f(b))
        print("Generated pair: {0}, {1}".format(x, y))

        # add 1 to count of points within the whole area
        total_area += 1.0

        if y <= f(x):
            area_under_curve += 1

    print("Rectangle area: {0}".format(REAL_AREA))
    if area_under_curve != 0.:
        print("Total area points: {0}".format(total_area))
        print("Area under curve points: {0}".format(area_under_curve))
        print("Calculated area: {0}".format(REAL_AREA * (area_under_curve / total_area)))


if __name__ == '__main__':
    print("Running Example numerics/example_1")
    main()
    print("Done...")