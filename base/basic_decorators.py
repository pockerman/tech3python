"""
Exposes various decorators
"""

import functools


def check_in_array(items):
    def check_matrix_name_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):

            if kwargs.get('name') not in items:
                raise ValueError("Name: " + kwargs.get('name') + " not in " + str(items))

            return f(*args, **kwargs)
        return wrapper
    return check_matrix_name_decorator
