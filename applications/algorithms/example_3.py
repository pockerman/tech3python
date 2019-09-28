"""
Category: Algorithms
ID: Example 3
Description: Fibonacci sequence calculation
Taken From: Code from the book: Coding Interviews: Questions, Analysis & Solutions

The Fibonacci sequence is given by
f(n) = 0 if n = 0
f(n) = 1 if n = 1
f(n) = f(n-1) + f(n-2) n>1
"""


def recursive_fib(n):
    """
    Recursive implementation of Fibonacci sequence
    :param n: The parameter that the sequence ends
    """

    if n < 0:
        raise ValueError("Cannot calculate Fibonacci sequence for negative numbers")

    if n == 0:
        return 0

    if n == 1:
        return 1

    return recursive_fib(n-1) + recursive_fib(n-2)


def iterative_fib(n):
    """
       Iterative implementation of Fibonacci sequence
       :param n: The parameter that the sequence ends
    """

    if n < 0:
        raise ValueError("Cannot calculate Fibonacci sequence for negative numbers")

    rslt = [0, 1]
    if n < 2:
        return rslt[n]

    rslt_previous = 1
    rslt_previous_previous = 0
    rslt_fib = 0

    for i in range(2, n+1, 1):
        rslt_fib = rslt_previous + rslt_previous_previous
        rslt_previous_previous = rslt_previous
        rslt_previous = rslt_fib

    return rslt_fib


def memo_fib(n):
    """
     Uses a dictionary to store the results of a recursive computation of the Fibonacci sequence
    :param n: The parameter that the sequence ends
    """
    rslt = {0:0, 1:1}
    if n not in rslt:
        rslt[n] = memo_fib(n-1) + memo_fib(n-2)
    return rslt[n]



def main():

    rslt = recursive_fib(5)
    assert rslt == 5, "Recursive Fibonacci: Invalid Fibonacci result {0} not equal to 5".format(rslt)

    rslt = iterative_fib(5)
    assert rslt == 5, "Iterative Fibonacci: Invalid Fibonacci result {0} not equal to 5".format(rslt)

    rslt = memo_fib(5)
    assert rslt == 5, "Memoization Fibonacci: Invalid Fibonacci result {0} not equal to 5".format(rslt)


if __name__ =='__main__':
    print("Running Example algorithms/example_3")
    main()
    print("Done...")