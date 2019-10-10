from .tree_base import TreeBase
from .tree_base import TreeNode
from predicates.basic_predicates import IsNonePredicate


class BinaryTree(TreeBase):

    """
    Models a binary tree
    """

    @staticmethod
    def n_children_per_node():
        return 2

    def __init__(self, insert_method, search_method):
        TreeBase.__init__(self, insert_method=insert_method, search_method=search_method)

    def push(self, value):

        """
        Adds a new value in the Binary tree. Insertion is done according to the
        insertion method specified at construction time
        """

        if self.get_root() is None:
            node = TreeNode(data=value, parent=None)
            node.set_children(children=[None, None])
            self._make_root(node)
            return

        predicate = IsNonePredicate()
        sucess = self._get_insert_method().insert(root=self._root, value=value, predicate=predicate)

        if sucess:
            self._size += 1

    def create(self, values):

        """
        Create a binary tree from the set of given values
        :param values: list of values
        """

        for item in values:
            self.push(value=item)