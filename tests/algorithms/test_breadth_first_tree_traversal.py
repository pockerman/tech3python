"""
Unit tests for breadth first tree traversal algorithm
"""
import unittest

from adt.tree_base import TreeNode
from algorithms.breadth_first_tree_traversal import BreadthFirstTreeSearch
from predicates.basic_predicates import IsNonePredicate
from predicates.basic_predicates import IdentityPredicate
from predicates.basic_predicates import HasValue


class BFSTreeTraversalTest(unittest.TestCase):

    """
    Test Scenario: Application attempts to traverse a tree with None root
    Expected Output: ValueError exception is raised
    """
    def test_none_root(self):
        node = None
        predicate = IdentityPredicate()
        with self.assertRaises(ValueError):
            BreadthFirstTreeSearch.traverse(root=node, predicate=predicate)

    """
        Test Scenario: Application attempts to traverse a tree with None predicate
        Expected Output: ValueError exception is raised
    """

    def test_none_predicate(self):
        node = TreeNode(data=None, parent=None)
        predicate = None
        with self.assertRaises(ValueError):
            BreadthFirstTreeSearch.traverse(root=node, predicate=predicate)

    """
    Test Scenario: Application attempts to traverse a tree with three nodes where the right child node satisfies the predicate
    Expected Output: The right child index,  and root should be returned 
    """
    def test_can_find_rightmost_node(self):
        root = TreeNode(data=10, parent=None)
        left_node = TreeNode(data=20, parent=root)
        left_node.set_children([None for i in range(2)])
        root.set_children([left_node, None])
        predicate = IsNonePredicate()

        theroot, child, idx = BreadthFirstTreeSearch.traverse(root=root, predicate=predicate)
        self.assertEqual(id(root), id(theroot), msg="Invalid root nodes")
        self.assertEqual(idx, 1, msg="Invalid child node id")

    """
    Test Scenario: Application attempts to traverse a tree with five nodes where the left child at level 1 satisfies the predicate
    Expected Output: The right child index,  and root should be returned 
    """

    def test_can_find_deeper_level_node(self):
        root = TreeNode(data=10, parent=None)
        left_node = TreeNode(data=20, parent=root)
        right_node = TreeNode(data=10, parent=root)
        right_node.set_children([None, None])

        left_left_node = TreeNode(data=60, parent=left_node)
        left_left_node.set_children([None, None])

        left_node.set_children([left_left_node, None])
        root.set_children([left_node, right_node])
        predicate = HasValue(60)

        theroot, child, idx = BreadthFirstTreeSearch.traverse(root=root, predicate=predicate)
        self.assertEqual(id(left_node), id(theroot), msg="Invalid root node")
        self.assertEqual(id(left_left_node), id(child), msg="Invalid child node")
        self.assertEqual(idx, 0, msg="Invalid child node id")


if __name__ == '__main__':
    unittest.main()