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

        """
        Returns the list of children of this node
        :return:
        """

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

        """
        Create a node having data = item and set the created node as the
        idx-th tree
        """
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

        if self._children is None:
            return True

        found=False
        for i in range(len(self._children)):
            if self._children[i] is not None:
                found = True
                break

        if found:
            return False
        return True

        # with Python 3.6 I am getting  TypeError: unhashable type: 'TreeNode'
        #return self._children is None or set(self._children) == set([None for i in range(len(self._children))])

    def contains_leaf(self):

        if self.is_leaf():
            return False, None

        for child in self.get_children():
            if child is not None and child.is_leaf():
                return True, child

        return False, None


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

    def has_value(self, value):

        """
        Returns True if the tree contains the given value
        """
        # find the node that holds the value
        predicate = HasValue(value=value)
        root, child, child_idx = self._search_method.traverse(root=self.get_root(), predicate=predicate)
        return child is not None

    def find(self, value):

        """
        Returns the node that has the given value
        """
        # find the node that holds the value
        predicate = HasValue(value=value)
        root, child, child_idx = self._search_method.traverse(root=self.get_root(), predicate=predicate)
        return child

    def delete(self, value):

        """
        Removes the given value in the ADT if present
        """
        # find the node that holds the value
        predicate = HasValue(value=value)

        parent, child, child_idx = self._search_method.traverse(root=self.get_root(), predicate=predicate)

        if parent is not child.get_parent():
            raise ValueError("Parent mismatch...")

        if child_idx is None:
            raise ValueError("Child id could not be found")

        # if we found a node that has this value we need to remove it
        if child is not None:

            #parent = child.get_parent()
            #child_idx = parent.which_child_am_i(child)

            # if this is a leaf then this is easy
            if child.is_leaf():

                # tell the parent that this child died
                parent.set_child(child_idx, None)
                self._size -= 1
                return True
            else:

                contains_leaf, child_leaf = child.contains_leaf()

                # does the node have a leaf?
                if contains_leaf:

                    # the node to be deleted contains a
                    # leaf. We will replace this node with the leaf
                    parent.set_child(idx=child_idx, item=child_leaf)
                    child_leaf.set_parent(parent=parent)

                    # tell the other children of child that they
                    # have a new father
                    children = child.get_children()
                    for the_child in children:
                        if the_child is not child_leaf:
                            the_child.set_parent(parent=child_leaf)
                            the_child_idx = child.which_child_am_i(the_child)

                            child_leaf.set_child(the_child_idx, the_child)

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