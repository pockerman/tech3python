"""
Unit tests for TreeBase
"""
import unittest

from adt.tree_base import TreeBase

class MockInsertMethod:
    def __init__(self):
        pass

    def insert(self, root, value):
        return True


class TreeBaseTest(unittest.TestCase):
    """
    Test Scenario: Application attempts to add a new value into the tree
    Expected Output: New item should be successfully inserted
    """

    def test_push_success(self):
        tb = TreeBase(insert_method=MockInsertMethod())
        self.assertEqual(len(tb), 0, msg="Tree size is not 0")
        tb.push(2)
        self.assertEqual(len(tb), 1, msg="Insert to "+type(tb).__name__+" failed")


if __name__ == '__main__':
    unittest.main()