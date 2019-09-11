"""
Basic predicates for querying the state of the passed object
in a uniform manner
"""

class IdentityPredicate:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        return True


class IsNonePredicate:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        return args[0] is None
