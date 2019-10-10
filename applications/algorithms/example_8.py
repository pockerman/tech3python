"""
Category: Algorithms
ID: Example 8
Description: Find the edit distance i.e. the number of operations required to transform one string to another
Taken From:

Details:

"""

import math


def get_edit_distance(string1, string2):

    if string1 is None or string2 is None:
        raise ValueError("None strings are not allowed")

    # no operations are needed if the strings
    # are equal
    if string1 == string2:
        return 0

    # if the first string is empty we need
    # as many operations as the number of characters in string2
    if string1 == "":
        return len(string2)

    count = 0

    for item in zip(string2, string1):
        if item[0] != item[1]:
            count += 1

    # we need to add the operations in the scenario
    # where string1 does not have the same length as string2
    if len(string1) != len(string2):
        count += int(math.fabs((len(string1) - len(string2))))

    return count


def main():

    try:
        get_edit_distance(None, "Alex")
    except ValueError as error:
        print(str(error))

    rslt = get_edit_distance("Alex", "Alex")
    print("For strings {0} {1} edit distance is {2} ".format("Alex", "Alex", rslt))
    rslt = get_edit_distance("", "Alex")
    print("For empty string and string {0} edit distance is {1} ".format( "Alex", rslt))
    rslt = get_edit_distance("Cat", "Alex")
    print("For empty strings {0} and {1} edit distance is {2} ".format("Cat", "Alex", rslt))

    rslt = get_edit_distance("Alex", "Cat")
    print("For empty strings {0} and {1} edit distance is {2} ".format("Alex", "Cat",  rslt))

    rslt = get_edit_distance("CatB", "CatA")
    print("For empty strings {0} and {1} edit distance is {2} ".format("CatB", "CatA", rslt))

    rslt = get_edit_distance("Cat", "CatA")
    print("For empty strings {0} and {1} edit distance is {2} ".format("Cat", "CatA", rslt))

if __name__ == '__main__':
    print("Running Example algorithms/example_8")
    main()
    print("Done...")