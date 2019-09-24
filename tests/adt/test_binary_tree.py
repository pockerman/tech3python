"""
Unit tests for BinaryTree class
"""

import unittest
from adt.binary_tree import BinaryTree
from algorithms.preorder_tree_traversal import PreorderTreeTraversal


class BinaryTreeTest(unittest.TestCase):
    """
    Test Scenario: Application attempts to add two new values into the tree that already has root using PreorderTraversal
    as an insertion policy
    Expected Output: New items should be successfully inserted
    """

    def test_push_success_preorder_traversal(self):

        bt = BinaryTree(insert_method=PreorderTreeTraversal)
        self.assertEqual(len(bt), 0,
                         msg="Tree size is not 0")

        # create the root
        bt.push(2)
        self.assertEqual(len(bt), 1,
                         msg="Insert to " + type(bt).__name__ + " failed")

        # now add the left node
        bt.push(3)
        self.assertEqual(len(bt), 2,
                         msg="Insert to " + type(bt).__name__ + " failed")

        self.assertIsNotNone(bt.get_root().get_child(0),
                             msg="Left child node of " + type(bt).__name__ + "should not be None ")

        self.assertEqual(bt.get_root().get_child(0).get_data(), 3,
                             msg="Invalid inserted data for " + type(bt).__name__)

        self.assertEqual(bt.get_root().get_child(0).get_level(), 1,
                         msg="Invalid node level {0} should be 1 ".format(bt.get_root().get_child(0).get_level()))

        # now add another node. Preorder traversal first scans the node and then the children
        bt.push(4)
        self.assertEqual(len(bt), 3,
                         msg="Insert to " + type(bt).__name__ + " failed")

        self.assertIsNotNone(bt.get_root().get_child(0).get_child(0),
                             msg="Left child node of " + type(bt).__name__ + "should not be None ")

        self.assertEqual(bt.get_root().get_child(0).get_child(0).get_data(), 4,
                            msg="Invalid inserted data for " + type(bt).__name__)

        self.assertEqual(bt.get_root().get_child(0).get_child(0).get_level(), 2,
                         msg="Invalid node level {0} should be 2 ".format(bt.get_root().get_child(0).get_child(0).get_level()))


if __name__ == '__main__':
    unittest.main()