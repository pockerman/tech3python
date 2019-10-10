"""
Category: Algorithms
ID: Example 9
Description: Find the number of 1s in the binary representation of an integer
Taken From: Code from the book Coding Interviews: Questions, Analysis & Solutions

Details:

"""


def count_ones(n):

    count = 0

    while n:
        count += 1
        n = (n-1) & n

    return count


def main():

    rslt = count_ones(99)
    print("For  {0}  number of ones is {1} ".format(99, rslt))

    rslt = count_ones(1)
    print("For  {0}  number of ones is {1} ".format(1, rslt))


if __name__ == '__main__':
    print("Running Example algorithms/example_9")
    main()
    print("Done...")