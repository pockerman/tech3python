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
            # we insert in the right subtree
            return self._do_insert(root.get_child(1), value=value, parent=root)

        elif root.data < value:
            # insert in the left subtree
            return self._do_insert(root.get_child(0), value=value, parent=root)

        # the data already exist
        return False

    def _do_insert(self, node, value, parent):

        if node is None:
            return TreeNode(data=value, parent=parent)

        if node.data > value:
            # we insert in the right subtree
            return self._do_insert(node.get_child(1), value=value, parent=parent)

        elif node.data < value:
            # insert in the left subtree
            return self._do_insert(node.get_child(1), value=value, parent=parent)

        return False


class BinarySearchTree(BinaryTree):

    """
    Binary Search Tree implementation
    """

    def __init__(self ):
        BinaryTree.__init__(self, insert_method=BSTInsertMethod(), search_method=None)
