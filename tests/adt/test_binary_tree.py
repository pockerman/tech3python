"""
Unit tests for BinaryTree class
"""

import unittest
from adt.binary_tree import BinaryTree
from algorithms.preorder_tree_traversal import PreorderTreeTraversal
from algorithms.breadth_first_tree_traversal import BreadthFirstTreeSearch


class BinaryTreeTest(unittest.TestCase):

    """
    Test Scenario: Application attempts to add two new values into the tree that already has root using PreorderTraversal
                   as an insertion policy
    Expected Output: New items should be successfully inserted
    """

    def test_push_success_preorder_traversal(self):

        bt = BinaryTree(insert_method=PreorderTreeTraversal, search_method=None)
        self.assertEqual(len(bt), 0,
                         msg="Tree size is not 0")

        # create the root
        bt.push(2)
        self.assertEqual(len(bt), 1, msg="Insert to " + type(bt).__name__ + " failed")

        # now add the left node
        bt.push(3)
        self.assertEqual(len(bt), 2, msg="Insert to " + type(bt).__name__ + " failed")

        self.assertIsNotNone(bt.get_root().get_child(0), msg="Left child node of " + type(bt).__name__ +
                                                             "should not be None ")

        self.assertEqual(bt.get_root().get_child(0).get_data(), 3, msg="Invalid inserted data for " + type(bt).__name__)

        self.assertEqual(bt.get_root().get_child(0).get_level(), 1, msg="Invalid node level {0} should be 1 ".format(bt.get_root().get_child(0).get_level()))

        # now add another node. Preorder traversal first scans the node and then the children
        bt.push(4)
        self.assertEqual(len(bt), 3, msg="Insert to " + type(bt).__name__ + " failed")

        self.assertIsNotNone(bt.get_root().get_child(0).get_child(0), msg="Left child node of " + type(bt).__name__ +
                                                                          "should not be None ")

        self.assertEqual(bt.get_root().get_child(0).get_child(0).get_data(), 4, msg="Invalid inserted data for " + type(bt).__name__)

        self.assertEqual(bt.get_root().get_child(0).get_child(0).get_level(), 2,
                         msg="Invalid node level {0} should be 2 ".format(bt.get_root().get_child(0).get_child(0).get_level()))

    """
       Test Scenario: Application attempts to add two new values into the tree that already has root using BreathFirstTraversal
                      as an insertion policy
       Expected Output: New items should be successfully inserted
    """

    def test_push_success_bfs_traversal(self):

        bt = BinaryTree(insert_method=BreadthFirstTreeSearch, search_method=None)
        self.assertEqual(len(bt), 0,  msg="Tree size is not 0")

        # create the root
        bt.push(2)
        self.assertEqual(len(bt), 1,
                         msg="Insert to " + type(bt).__name__ + " failed")

        # now add the left node
        bt.push(3)
        self.assertEqual(len(bt), 2, msg="Insert to " + type(bt).__name__ + " failed")

        self.assertIsNotNone(bt.get_root().get_child(0), msg="Left child node of " + type(bt).__name__ +\
                                                             "should not be None ")

        self.assertEqual(bt.get_root().get_child(0).get_data(), 3, msg="Invalid inserted data for " + type(bt).__name__)

        self.assertEqual(bt.get_root().get_child(0).get_level(), 1, msg="Invalid node level {0} should be 1 ".format(bt.get_root().get_child(0).get_level()))

        # now add another node. BFS traversal should add this to the right child of the root
        bt.push(4)
        self.assertEqual(len(bt), 3, msg="Insert to " + type(bt).__name__ + " failed")

        self.assertIsNotNone(bt.get_root().get_child(1), msg="Right child node of " + type(bt).__name__ +
                                                             "should not be None ")

        self.assertEqual(bt.get_root().get_child(1).get_data(), 4, msg="Invalid inserted data for " + type(bt).__name__)

        self.assertEqual(bt.get_root().get_child(1).get_level(), 1, msg="Invalid node level {0} should be 2 ".format(bt.get_root().get_child(1).get_level()))

    """
    Test Scenario: Application creates a BinaryTree and adds nodes using BreathFirstTraversal as an insertion policy.
                    It then deletes on of the leaf nodes
    Expected Output: Deleted node should be removed. 
    """
    def test_delete_leaf_node_bfs_traversal(self):

        bt = BinaryTree(insert_method=BreadthFirstTreeSearch, search_method=BreadthFirstTreeSearch)
        self.assertEqual(len(bt), 0, msg="Tree size is not empty")

        bt.create([i+1 for i in range(11)])
        self.assertEqual(len(bt), 11, msg="Invalid Tree size")
        bt.delete(value=9)
        self.assertEqual(len(bt), 10, msg="Invalid Tree size")


if __name__ == '__main__':
    unittest.main()