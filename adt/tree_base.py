"""
Base class for implementing trees
"""
from .adt_base import ADTBase


class TreeNode:
    """
    Helper class for deriving Tree Nodes
    """

    def __init__(self, data, parent):
        self._data = data
        self._parent = parent
        self._children = None
        self._level = 0

        if self._parent is not None:
            self._level = self._parent.get_level() + 1

    def set_child(self, idx, item):
        self._children[idx] = item

    def get_child(self, idx):
        return self._children[idx]

    def set_children(self, children):
        self._children = children

    def get_children(self):
        if self._children is None:
            raise AttributeError("Children is None")
        return self._children

    def n_children(self):
        if self._children is None:
            return 0
        return len(self._children)

    def get_level(self):
        return self._level

    def has_parent(self):
        """
        Returns True if the parent of this node is not None
        """
        return self._parent is not None


class TreeBase(ADTBase):

    def __init__(self, insert_method):
        super(TreeBase, self).__init__()
        self._size = 0
        self._root = None
        self._insert_method = insert_method

    def __len__(self):
        """
        Returns the number of elements present in the ADT
        """
        return self._size

    def empty(self):
        """
        Returns true if the ADT is empty
        """
        return self._size == 0

    def get_root(self):
        """
        Returns the root node
        :return:
        """
        return self._root

    def _make_root(self, node):
        self._root = node
        self._size += 1

    def _get_insert_method(self):
        return self._insert_method