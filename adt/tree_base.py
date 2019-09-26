"""
Base class for implementing trees
"""
from .adt_base import ADTBase
from predicates.basic_predicates import HasValue


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
            self._children = [None for i in range(parent.n_children())]

    def __eq__(self, other):
        return id(self) == id(other)

    @property
    def value(self):
        return self._data

    def set_data(self, data):

        """
        Set the data stored by this node
        """
        self._data = data

    def get_data(self):

        """
        Returns the data stored by the node
        """
        return self._data

    def set_child(self, idx, item):

        """
        Set the idx-th child of this node
        """
        self._children[idx] = item

    def get_child(self, idx):

        """
        Get the idx-th child
        """
        return self._children[idx]

    def set_children(self, children):

        """
        Set the children of this node
        :param children: A list of children
        """
        self._children = children

    def get_children(self):
        if self._children is None:
            raise AttributeError("Children is None")
        return self._children

    def n_children(self):

        """
        Returns the number of children of the node
        """
        if self._children is None:
            return 0
        return len(self._children)

    def get_level(self):

        """
        Returns the level of the node
        """
        return self._level

    def has_parent(self):

        """
        Returns True if the parent of this node is not None
        """
        return self._parent is not None

    def set_parent(self, parent):

        """
        Set the parent node
        """
        self._parent = parent

        # by setting the parent implicitly we set the level also
        if self._parent is not None:
            self._level = self._parent.get_level() + 1

    def get_parent(self):

        """
        Returns the parent for this node
        """

        return self._parent

    def create_and_set_child(self, idx, item):
        node = TreeNode(data=item, parent=self)
        node.set_children(children=[None for i in range(self.n_children())])
        self.set_child(idx, node)

    def which_child_am_i(self, child):

        if id(child) == id(self):
            return -1

        for c in range(self.n_children()):
            if id(self.get_child(c)) == id(child):
                return c

        return None

    def is_leaf(self):

        """
        Returns True if this Node is a leaf
        """
        return self._children is None or set(self._children) == set([None for i in range(len(self._children))])


class TreeBase(ADTBase):

    """
    Base class for trees
    """

    def __init__(self, insert_method, search_method):
        super(TreeBase, self).__init__()
        self._size = 0
        self._root = None
        self._insert_method = insert_method
        self._search_method = search_method

    def __len__(self):

        """
        Returns the number of elements present in the tree
        """
        return self._size

    def set_search_method(self , method):

        """
        Set the search method that the ADT is using to
        search its contents
        """
        self._search_method = method

    def empty(self):

        """
        Returns true if the tree is empty
        """
        return self._size == 0

    def get_root(self):

        """
        Returns the root node
        """
        return self._root

    def delete(self, value):

        """
        Removes the given value in the ADT if present
        """
        # find the node that holds the value
        predicate = HasValue(value=value)

        root, child, child_idx = self._search_method.traverse(root=self.get_root(), predicate=predicate)

        # if we found a node that has this value we need to remove it
        if child is not None:

            # if this is a leaf then this is easy
            if child.is_leaf():
                parent = child.get_parent()
                child_idx = parent.which_child_am_i(child)

                if child_idx is None:
                    raise ValueError("Child id could not be found")

                # tell the parent that this child died
                parent.set_child(child_idx, None)
                self._size -= 1
                return True
        return False

    def _make_root(self, node):

        """
        Assign the given node as the root of the tree
        """

        self._root = node
        self._size += 1

    def _get_insert_method(self):

        """
        Returns the insertion method used by the tree
        """
        return self._insert_method