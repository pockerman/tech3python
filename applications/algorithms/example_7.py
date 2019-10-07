"""
Category: Algorithms
ID: Example 7
Description: Find the number of digits in a given integer
Taken From:

Details:

We can get the number of digits contained in an integer by continuously
dividing with 10 as long as the number is greater than 0
"""


def compute(n):

    if type(n) != int:
        raise ValueError(" The given number is not an integer")

    sum = 0
    number = n

    while number > 0:
        number = number // 10
        sum += 1

    print("Number of digits in number {0} is {1}".format(n, sum))


def main():

    compute(n=100)
    compute(n=1210)
    compute(n=1)


if __name__ == '__main__':
    print("Running Example algorithms/example_7")
    main()
    print("Done...")