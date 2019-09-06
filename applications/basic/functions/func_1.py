"""
Variable arguments
"""

from inspect import getfullargspec

def add_to_cart(*items):
    return items


print(getfullargspec(add_to_cart()))
cart = add_to_cart('item 1')
print(cart)
cart = add_to_cart('item 1', 'item 2', 'item 3', 'item 4')
print(cart)



