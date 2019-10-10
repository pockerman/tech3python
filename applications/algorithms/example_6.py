"""
Category: Algorithms
ID: Example 6
Description: Find the majority element in an array
Taken From: Code from the book Coding Interviews: Questions, Analysis & Solutions

Details:

The majority element is an element that occurs from more than half of the size of the array.
As an example we can consider the array {5, 6, 5, 2, 9, 5, 5, 5, 7}. Then the number 5 is the
majority element because it appears five times whilst the array has size 9.

Here are a few ways to solve the problem

- 1) sort the array, in time O(Nlog(N)), Count the occurences in O(n) time
- 2) Use the partition method: If there is a majority element in an array, then the majority
     element should occur in the middle of the array when this is sorted this is because an element
     is a majority element if it occurs more than  half of the size of the array.
     Hence the majority of an array is also the median of the array, which is:
      - the (n/2)th number in an array with n elements.
     There exists an O(N) algorithm to get the k-th number in an array. It is related
     to the quicksort algorithm
"""

import random

def swap(array, i, j):
    # swap
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def partition(array, start, end):

    pivot = random.randint(start, end)
    swap(array, pivot, end)

    small = start - 1
    for i in range(start, end+1, 1):

        if array[i] < array[end]:
            small += 1
            if i != small:
                swap(array, small, i)

    small += 1
    if small != end:
        swap(array, small, end)

    return small


def check_majority_existence(array, element):
    """
    O(N) checks if the element is the majority element in the array
    :param array: array to search into
    :param element: the element to test
    :return: True if the element occurs more than len(array)/2. False otherwise
    """
    is_majority = False
    count = 0
    for item in array:

        if item == element:
            count += 1

            if count > len(array)//2:
                is_majority = True
                break
    return is_majority

def find_majority_element(array):
    """
    Find the majority element if it exists in the given array
    :param array: the array to search for
    :return: the majority element if it exists
    """

    start = 0
    end = len(array)-1
    idx_middle = len(array) >> 1

    idx = partition(array, start, end)

    while idx != idx_middle:

        if idx > idx_middle:
            end = idx - 1
            idx = partition(array, start, end)
        else:
            start = idx + 1
            idx = partition(array, start, end)

    rslt = array[idx_middle]

    if check_majority_existence(array, rslt):
        return rslt

    print("\t Could not determine majority element in array")
    return None


def find_majority_element_2(array):
    rslt = array[0]
    count = 1

    for i in range(1, len(array)):
        if count == 0:
            rslt = array[i]
            count = 1
        elif array[i] == rslt:
            count += 1
        else:
            count -= 1

    if check_majority_existence(array, rslt):
        return rslt

    print("\t Could not determine majority element in array")
    return None


def main():
    array = [5, 6, 5, 2, 9, 5, 5, 5, 7]

    idx = find_majority_element(array=array)
    print("Majority element in {0} is {1}".format(array, idx))

    print("Using second approach...")
    idx = find_majority_element_2(array=array)
    print("Majority element in {0} is {1}".format(array, idx))


if __name__ == '__main__':
    print("Running Example algorithms/example_6")
    main()
    print("Done...")