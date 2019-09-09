from .tree_base import TreeBase
from .tree_base import TreeNode


class BinaryTree(TreeBase):

    def __init__(self, insert_method):
        TreeBase.__init__(self, insert_method=insert_method)

    def push(self, value):
        """
        Adds a new value in the ADT. Concrete classes specify
        where the push occurs
        """

        if self.get_root() is None:
            node = TreeNode(data=value, parent=None)
            node.set_children(children=[None, None])
            self._make_root(node)
            return

        sucess = self._insert_method.insert(root=self._root, value=value)

        if sucess:
            self._size += 1