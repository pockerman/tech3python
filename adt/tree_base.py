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

    def set_child(self, idx, item):
        self._children[idx] = item

    def n_children(self):
        return len(self._children)

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

    def push(self, value):
        """
        Adds a new value in the ADT. Concrete classes specify
        where the push occurs
        """
        sucess = self._insert_method.insert(root=self._root, value=value)

        if sucess:
            self._size += 1


    def get_root(self):
        """
        Returns the root node
        :return:
        """
        return self._root