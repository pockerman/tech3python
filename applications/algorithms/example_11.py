"""
Category: Algorithms
ID: Example 11
Description: Given two integers m and n calculate the number of bits that need to
be modified to change m to n
Taken From: Code from the book Coding Interviews: Questions, Analysis & Solutions

Details:

Consider the number 14 its binary representation is 1110 and number 11 1011. We need to modify
two bits of 1011 to get to 1110 in binary. The bitwis XOR gets 1 when the two input bits
are different and gets 0 when they are the same. Thus, XOR indicates the bit difference of m and n
We can count the number of 1's in the resulting XOR to see how many bits we need to change

"""


def count_bits(m, n):

    rslt = m^n

    count = 0

    while rslt:
        count += 1
        rslt = (rslt - 1) & rslt

    return count


def main():

    rslt = count_bits(4, 3)
    print("Number of bits to change {0} to {1} is {2}".format(4, 3, rslt))

    rslt = count_bits(10, 13)
    print("Number of bits to change {0} to {1} is {2}".format(10, 13, rslt))

    rslt = count_bits(14, 11)
    print("Number of bits to change {0} to {1} is {2}".format(14, 11, rslt))


if __name__ == '__main__':
    print("Running Example algorithms/example_11")
    main()
    print("Done...")