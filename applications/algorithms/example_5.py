"""
Category: Algorithms
ID: Example 5
Description: Find the index of turning point in a unimodal array
Taken From: Code from the book: Coding Interviews: Questions, Analysis & Solutions

Details:

A unimodal array is an array that increases and then decreases.

The binary search algorithm is suitable for searching in a sorted array.
In this scenario, the array is partially sorted.

The algorithm starts with the middle element and attempts to find in which sub-array
it belongs so as to discard the remaining elements in the sub-array

The algorithm repeatedly attempts to discard elements until the solution is found

"""


def find_turn_point_idx(array):

    if len(array) <= 2:
        raise ValueError("Cannot work with an array of length 2")

    p1 = 0
    p2 = len(array)-1


    while p2 > p1 + 1:

        idx_middle = (p1 + p2)//2

        if idx_middle == 0 and  idx_middle == len(array)-1:
            return None

        if array[idx_middle] > array[idx_middle - 1] and array[idx_middle] > array[idx_middle + 1]:
            return idx_middle
        elif array[idx_middle] > array[idx_middle - 1] and array[idx_middle] < array[idx_middle + 1]:
            p1 = idx_middle
        else:
            p2 = idx_middle

    return None


def main():
    array = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
    idx = find_turn_point_idx(array=array)

    # should print 5
    print("Turning point in {0} is {1}".format(array, idx))


if __name__ == '__main__':
    print("Running Example algorithms/example_5")
    main()
    print("Done...")