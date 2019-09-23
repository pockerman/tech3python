"""
Preorder tree traversal algorithm
"""


class PreorderTreeTraversal:

    @staticmethod
    def traverse(root, predicate):

        """
        Preorder traversal algorithm
        """
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

            root, child, _ = PreorderTreeTraversal.traverse(child, predicate)

            if predicate(child):
                idx = c
                break

        return root, child, idx

    @staticmethod
    def insert(root, value, predicate):

        """
        Insert the given value in the tree represented by the root.
        Insertion position is determined by the given predicate
        """
        root, child, idx = PreorderTreeTraversal.traverse(root, predicate)

        if child is None:
            root.create_and_set_child(idx, value)
            return True

        child.set_data(data=value)
        child.set_parent(parent=root)
        root.set_child(idx, item=child)
        return True

    def __call__(self, *args, **kwargs):
        self.insert(root=args[0], value=args[1], predicate=args[2])



