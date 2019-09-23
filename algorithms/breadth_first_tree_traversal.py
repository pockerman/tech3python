
from collections import deque

class BreadthFirstTreeSearch:

    """
    Implement BFS tree traversal
    """

    @staticmethod
    def traverse(root, predicate):

        """
        Traverse the tree rooted at root and find the first node
        that satisfies the given predicate
        """

        if root is None:
            raise ValueError("Root node is None")

        if predicate is None:
            raise ValueError("Predicate is None")

        queue = deque()
        queue.append(root)

        child = None
        child_root = root
        idx = -1

        while len(queue) != 0:

            child = queue.popleft()

            if predicate(child):

                if child is not None:
                    child_root = child.get_parent()
                    
                # if all children of the root are None simply return
                # the first index
                idx = child_root.which_child_am_i(child)
                break
            else:
                for c in range(child.n_children()):
                    queue.append(child.get_child(c))

        return child_root, child, idx