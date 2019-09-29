"""
Category: Algorithms
ID: Example 4
Description: Find the minimum element between two increasingly sorted sub-arrays
            comming from a rotation of the main array
Taken From: Code from the book: Coding Interviews: Questions, Analysis & Solutions

Details:

The algorithm utilizes two pointers P1 and P2

P1->first element in the array
P2->last element in the array

Compare then the number in the middle with the numbers pointed to by P1 and P2:

- if the middle number is in the first increasingly sorted sub-array it is greater
than or equal to the number pointed to by P1
Thus, the minimal number is behind the middle number in the array. Hence we should move P1 to the middle and continue to
search numbers between P1 and P2 recursively.

- If the middle number is in the second sub-array, it is less than or equal to the number pointed to by P2
The minimal number is before the middle number in the array in such cases so it moves P2 to the middle.
We continue to search recursively because P1 points to a number in the first sub-array and P2 points to a number in the
second sub-array


No matter if it moves P1 or P2 for the next round of search, half of the array is excluded. It stops
searching when P1 points to the last number of the first sub-array and P2 points to the first number of the
second sub-array, which is also the minimum of the array.

"""


def find_min(array):

    p1 = 0
    p2 = len(array)-1
    idx_middle = p1

    while array[p1] >= array[p2]:
        if(p2 - p1 == 1):
            idx_middle = p2
            break

        idx_middle = (p1 + p2)//2

        if array[p1] == array[p2] and  array[idx_middle] == array[idx_middle]:
            print("\tCannot find minimum sequential scan is needed")
            idx_middle = None
            break

        if array[idx_middle] >= array[p1]:
            p1 = idx_middle
        elif array[idx_middle] <= array[p2]:
            p2 = idx_middle

    if idx_middle is not None:
        return array[idx_middle]

    return None


def main():
    array = [3, 4, 5, 1, 2]
    min = find_min(array=array)
    print("Min element in {0} is {1}".format(array, min))

    # Let’s look at the following example
    # {1, 0, 1, 1, 1} this is a rotation of
    # the increasingly sorted array
    # {0, 1, 1, 1, 1}. In this case the elements pointed
    # to by P1 and P2, as well as the middle element, are all 1.
    # The middle element with index 2 is in the second sub-array
    # Therefore, the algorithm cannot determine if the middle element
    # belongs to the first or second sub-array when the middle element and the
    # two numbers pointed to by P1 and P2 are equal, and it cannot move pointers
    # to narrow the search range.It has to search sequentially in such a scenario.
    array = [1, 0, 1, 1, 1]
    min = find_min(array=array)
    print("Min element in {0} is {1}".format(array, min))


if __name__ == '__main__':
    print("Running Example algorithms/example_4")
    main()
    print("Done...")