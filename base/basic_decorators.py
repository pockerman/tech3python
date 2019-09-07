"""
Exposes various decorators
"""

import functools


def check_in_array(items):
    def check_name_in_items_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):

            if kwargs.get('name') not in items:
                raise ValueError("Name: " + kwargs.get('name') + " not in " + str(items))

            return f(*args, **kwargs)
        return wrapper
    return check_name_in_items_decorator


def check_not_none(msg: str):
    def check_not_none_item_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if kwargs.get('item') is None:
                raise ValueError(msg)
            return f(*args, **kwargs)
        return wrapper
    return check_not_none_item_decorator


def check_array_index(array):
    def check_index_decorator(f):
        def wrapper(*args, **kwargs):
            if kwargs.get('idx') > len(array):
                raise IndexError("Index: ", kwargs.get('idx'), " not in [0, ", len(array), ")" )
            return f(*args, **kwargs)
        return wrapper
    return check_index_decorator

