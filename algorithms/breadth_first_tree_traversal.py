
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
        queue.append((root, 0))

        child = None
        child_parent = root
        idx = -1

        # potential parents in a given level
        parent_per_level = dict()
        current_level = root.get_level()
        parent_per_level[current_level] = [root]

        while len(queue) != 0:

            item = queue.popleft()
            child = item[0]

            if child is not None and child.get_level() not in parent_per_level.keys():
                parent_per_level[child.get_level()] = [child]
            elif child is not None and child.get_parent() is not None and  child.get_parent() not in parent_per_level[child.get_level()]:
                parent_per_level[child.get_level()].append(child)

            child_level = item[1]

            if predicate(child):

                # get all the candidate parents of this child
                child_parents = parent_per_level[child_level-1 if child_level > 0 else child_level]

                # try to find the parent that has the child
                stop = False
                for parent in child_parents:

                    idx = parent.which_child_am_i(child)

                    if idx is not None and idx is not -1:
                        child_parent = parent
                        stop = True
                        break

                if stop:
                    break
            else:

                if child is not None:
                    for c in range(child.n_children()):
                        queue.append((child.get_child(c), child.get_level() +1))

        return child_parent, child, idx

    @staticmethod
    def insert(root, value, predicate):

        """
        Insert the given value in the tree represented by the root.
        Insertion position is determined by the given predicate
        """
        root, child, idx = BreadthFirstTreeSearch.traverse(root, predicate)

        if child is None:
            root.create_and_set_child(idx, value)
            return True

        child.set_data(data=value)
        child.set_parent(parent=root)
        root.set_child(idx, item=child)
        return True

    def __call__(self, *args, **kwargs):
        return self.insert(root=args[0], value=args[1], predicate=args[2])