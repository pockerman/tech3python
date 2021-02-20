"""
Unit tests for BinarySearchTree class
"""

import unittest
from adt.binary_search_tree import BinarySearchTree


class BinarySearchTreeTest(unittest.TestCase):
    """
    Unit tests for BinarySearchTree
    """

    """Test Scenario: Application creates a new BST 
        Expected Output: Root node should be properly created
    """
    def test_create_root(self):

        tree =  BinarySearchTree()
        tree.push(value=10)

        self.assertEqual(len(tree), 1, "Invalid tree size {0} should be {1}".format(len(tree), 1))

        root = tree.get_root()
        self.assertIsNotNone(root, "Root node was not created for BST")
        self.assertEqual(root.data, 10, "Root node for BST has incorrect data. Should have {0} but has {1}".format(10, root.data))

    """Test Scenario: Application attempts to add an item that should be at the left sub-tree
           Expected Output: New node should be properly inserted
    """

    def test_add_new_node_left_sub_tree(self):
        tree = BinarySearchTree()
        tree.push(value=10)

        root = tree.get_root()
        self.assertIsNotNone(root, "Root node was not created for BST")
        self.assertEqual(root.data, 10,
                         "Root node for BST has incorrect data. Should have {0} but has {1}".format(10, root.data))

        tree.push(value=9)
        node = root.get_child(0)

        self.assertEqual(len(tree), 2, "Invalid tree size {0} should be {1}".format(len(tree), 2))
        self.assertIsNotNone(node, "Left node was not created for BST")
        self.assertEqual(node.data, 9,
                         "Left node for BST has incorrect data. Should have {0} but has {1}".format(9, node.data))

    """Test Scenario: Application attempts to add an item that should be at the right sub-tree
        Expected Output: New node should be properly inserted
    """
    def test_add_new_node_right_sub_tree(self):
        tree = BinarySearchTree()
        tree.push(value=10)

        root = tree.get_root()
        self.assertIsNotNone(root, "Root node was not created for BST")
        self.assertEqual(root.data, 10,
                         "Root node for BST has incorrect data. Should have {0} but has {1}".format(10, root.data))

        tree.push(value=11)
        node = root.get_child(1)

        self.assertEqual(len(tree), 2, "Invalid tree size {0} should be {1}".format(len(tree), 2))
        self.assertIsNotNone(node, "Right node was not created for BST")
        self.assertEqual(node.data, 11,
                         "Right node for BST has incorrect data. Should have {0} but has {1}".format(11, node.data))

    """Test Scenario: Application attempts to add an item that already exists in the tree
        Expected Output: New node should not be inserted
    """
    def test_add_new_node_with_same_value(self):
        tree = BinarySearchTree()
        tree.push(value=10)

        root = tree.get_root()
        self.assertIsNotNone(root, "Root node was not created for BST")
        self.assertEqual(root.data, 10,
                         "Root node for BST has incorrect data. Should have {0} but has {1}".format(10, root.data))

        tree.push(value=10)
        self.assertEqual(len(tree), 1, "Invalid tree size {0} should be {1}".format(len(tree), 1))

    """Test Scenario: Application attempts to build a BST from a given set of values
        Expected Output: BST should be properly created
    """
    def test_bst_from_unique_values(self):
        tree = BinarySearchTree()

        values = [10, 9, 15, 7, 14, 16, 6, 8, 12, 17, 13]
        tree.create(values=values)
        self.assertEqual(len(tree), len(values), "Invalid tree size {0} should be {1}".format(len(tree), len(values)))

        # let's check the internals
        for item in values:
            node = tree.find(value=item)
            self.assertIsNotNone(node, "Node with value {0} should not be None".format(item))

            child0 = node.get_child(0)
            child1 = node.get_child(1)
            parent = node.get_parent()

            if item == 10:
                self.assertIsNotNone(child0, "Left child should not be None for value".format(item))
                self.assertIsNotNone(child1, "Right child should not be None for value".format(item))
                self.assertIsNone(parent, "Parent  should be None for value".format(item))
            elif item == 9:
                self.assertIsNotNone(child0, "Left child should not be None for value".format(item))
                self.assertEqual(child0.data, 7, "Child  item should be {0} but is {1}".format(7, child0.data))
                self.assertIsNone(child1, "Right child should  be None for value".format(item))
                self.assertIsNotNone(parent, "Parent  should not be None for value".format(item))
                self.assertEqual(parent.data, 10, "Parent  item should be {0} but is {1}".format(10, parent.data))


if __name__ == '__main__':
    unittest.main()