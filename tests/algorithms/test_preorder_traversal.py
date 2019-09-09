"""
Unit tests for preorder traversal algorithm
"""
import unittest

from algorithms.preorder_tree_traversal import preorder_traversal
from predicates.identity_predicate import IdentityPredicate
from adt.tree_base import TreeNode

class PreorderTraversalTest(unittest.TestCase):
    """
    Unit test for preorder traversal
    """

    """
    Test Scenario: Application attempts to apply preorder traversal with no root
    Expected Output: ValueError exception should be raised
    """
    def test_root_is_None(self):
        node = None
        predicate = IdentityPredicate()
        with self.assertRaises(ValueError):
            preorder_traversal(root=node, predicate=predicate)

    """
      Test Scenario: Application attempts to apply preorder traversal with no predicate
      Expected Output: ValueError exception should be raised
    """

    def test_predicate_is_None(self):
        node = TreeNode(data=0, parent=None)
        predicate = None
        with self.assertRaises(ValueError):
            preorder_traversal(root=node, predicate=predicate)


if __name__ == '__main__':
    unittest.main()