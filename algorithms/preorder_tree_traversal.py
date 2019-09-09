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
    
    for c in root.children():
        node = preorder_traversal(c , predicate)

        if node is not None:
            break

    return node


