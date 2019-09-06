"""
Python uses the C3 algorithm to figure out the class
inheritance. Code from the book: Pro Python 3, 3rd Edition
"""

def c_3(cls, *mro_lists):
    """
    Implement the C3 algorithm
    """

    # make a copy of the lists
    mro_lists = [list(mro_list[:]) for mro_list in mro_lists]

    # the new MRO with the class itself
    mro = [cls, ]

    return mro