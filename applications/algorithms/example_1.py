"""
Algorithms Example 1

Python uses the C3 algorithm to figure out the class
inheritance. Code from the book: Pro Python 3, 3rd Edition
"""

import itertools

def c_3(cls, *mro_lists):
    """
    Implement the C3 algorithm
    """

    # make a copy of the lists
    mro_lists = [list(mro_list[:]) for mro_list in mro_lists]

    # the new MRO with the class itself
    mro = [cls, ]

    while True:

        candidate_found = False
        for mro_list in mro_lists:

            if not len(mro_list):
                continue

            if candidate_found:
                if candidate in mro:
                    mro_list.pop(0)
                continue

            candidate = mro_list[0] # the potential candiadate for MRO

            if candidate in itertools.chain(*(x[1:] for x in mro_lists)):
                continue
            else:

                # candidate is valid so promote to MRO
                mro.append(candidate)
                mro_list.pop(0)
                candidate_found = True

        if not sum(len(mro_list) for mro_list in mro_lists):
            # there are no MROs to cycle through
            break

        if not candidate_found:
            # No valid candidate was available, so we have to bail out.
            break
            raise TypeError("Inconsistent MRO")

    return mro


if __name__ == '__main__':

    # should print ['C', 'B', 'A', 'object']
    print(c_3('C', ['B', 'A', 'object'], ['A', 'object'], ['B', 'A']))