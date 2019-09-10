"""
Unit tests for preorder traversal algorithm
"""
import unittest

from algorithms.preorder_tree_traversal import preorder_traversal
from predicates.basic_predicates import IdentityPredicate
from predicates.basic_predicates import IsNonePredicate
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

    """
    Test Scenario: Application attempts to apply preorder traversal with a valid root and IsNonePredicate
    on a root with two None children
    Expected Output: None should be returned
    """
    def test_none_children_can_be_found(self):
        node = TreeNode(data=0, parent=None)
        node.set_children([None, None])
        predicate = IsNonePredicate()
        root, found, idx = preorder_traversal(root=node, predicate=predicate)
        self.assertIsNone(found, "Could not find None child")
        self.assertEqual(idx, 0)

    """
       Test Scenario: Application attempts to apply preorder traversal with a valid root and IsNonePredicate
       on a root with two children. The right children is None
       Expected Output: None should be returned
    """

    def test_none_child_can_be_found(self):
        node = TreeNode(data=0, parent=None)
        child1 = TreeNode(data=10, parent=node)
        node.set_children([child1, None])
        predicate = IsNonePredicate()
        root, found, idx = preorder_traversal(root=node, predicate=predicate)
        self.assertIsNone(found, "Could not find None child")
        self.assertEquals(idx, 1)



if __name__ == '__main__':
    unittest.main()