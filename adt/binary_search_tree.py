"""
module: binary_search_tree implements a binary search tree
"""

from .binary_tree import BinaryTree
from .tree_base import TreeNode


class BSTInsertMethod:

    def __init__(self):
        pass

    def insert(self, root, value, predicate):

        if root is None:
            return TreeNode(data=value, parent=None)

        if root.data > value:
            # we insert in the left subtree
            return self._do_insert(root.get_child(0), value=value, parent=root)

        elif root.data < value:
            # insert in the right subtree
            return self._do_insert(root.get_child(1), value=value, parent=root)

        # the data already exist
        return False

    def _do_insert(self, node, value, parent):

        if node is None:

            if parent.data > value:
                child_idx = 0
            elif parent.data < value:
                child_idx = 1
            else:
                raise ValueError("Attempt to add a value that already exists")

            node = TreeNode(data=value, parent=parent)
            parent.set_child(idx=child_idx, item=node)

            return node

        if node.data > value:
            # we insert in the left subtree
            return self._do_insert(node.get_child(0), value=value, parent=node)

        elif node.data < value:
            # insert in the right subtree
            return self._do_insert(node.get_child(1), value=value, parent=node)

        return False

class BSTSearchMethod:


    def traverse(self, root, predicate):

        if predicate(root):

            if root.get_parent() is not None:
                return root.get_parent(), root, root.get_parent().which_child_am_i(root)
            else:
                return root.get_parent(), root, None

        if root.data > predicate.value:
            return self.traverse( root.get_child(0), predicate)

        if root.data < predicate.value:
            return self.traverse( root.get_child(1), predicate)


class BinarySearchTree(BinaryTree):

    """
    Binary Search Tree implementation
    """

    def __init__(self ):
        BinaryTree.__init__(self, insert_method=BSTInsertMethod(), search_method=BSTSearchMethod())
