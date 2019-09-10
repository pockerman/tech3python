"""
Preorder tree traversal algorithm
"""

def preorder_traversal(root, predicate):

    if root is None:
        raise ValueError("Root node is None")

    if predicate is None:
        raise ValueError("Predicate is None")

    if predicate(root):
        return root

    child = None
    idx = -1

    for c in range(root.n_children()):

        child = root.get_child(c)

        if predicate(child):
            idx = c
            break

        child = preorder_traversal(child, predicate)

    return root, child, idx


