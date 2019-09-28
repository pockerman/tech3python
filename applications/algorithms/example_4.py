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
searching when P1 points to the last number of the first sub-array and P 2 points to the first number of the
second sub-array, which is also the minimum of the array.

"""