"""
Category: Algorithms
ID: Example 10
Description: Find whether a number is a power product of 2
Taken From: Code from the book Coding Interviews: Questions, Analysis & Solutions

Details:

A number that can be written as 2^k will only have one bit
with the value of 1 in its binary representation we can remove that
by applying (n-1) & n

"""


def is_power_product_of_2(n):

    return n != 0 and (n-1) & n == 0


def main():

    rslt = is_power_product_of_2(4)
    print("{0}  is  power product of 2? {1} ".format(4, rslt))

    rslt = is_power_product_of_2(1)
    print("{0}  is  power product of 2? {1} ".format(1, rslt))

    rslt = is_power_product_of_2(5)
    print("{0}  is  power product of 2? {1} ".format(5, rslt))


if __name__ == '__main__':
    print("Running Example algorithms/example_10")
    main()
    print("Done...")