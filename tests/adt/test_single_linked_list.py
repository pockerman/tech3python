import unittest

from adt.single_linked_list import SinglyLinkedList
from adt.single_linked_list import SingleLinkedListNode


class TestSinglyLinkedList(unittest.TestCase):

    def test_push(self):

        """
        Test Scenario: Application creates a single linked list and attempts to
        add an element at the top
        Expected Output: Item should be properly added
        """

        slist = SinglyLinkedList()
        node = slist.push(value=2)
        self.assertEqual(slist.size(), 1)
        self.assertEqual(id(node), id(slist.head()))

    def test_delete_node_null(self):

        """
        Test Scenario: Application creates a single linked list and attempts to
        delete a None element from the list
        Expected Output: Deletion should not occur
        """

        slist = SinglyLinkedList()
        result = slist.delete_node(node=None)
        self.assertEqual(result, False)

    def test_delete_node_head_null(self):

        """
        Test Scenario: Application creates a single linked list and attempts to
        delete a node from the empty list
        Expected Output: Deletion should not occur
        """

        slist = SinglyLinkedList()
        node = SingleLinkedListNode(data=2, next_node=None)
        result = slist.delete_node(node=node)
        self.assertEqual(result, False)

    def test_delete_node(self):

        """
        Test Scenario: Application creates a single linked list and inserts a node. It then attempts to
        delete the node from the list
        Expected Output: Deletion should  occur
        """

        slist = SinglyLinkedList()
        node = slist.push(value=10)
        self.assertIsNotNone(node, "Could not insert to list correctly")
        result = slist.delete_node(node=node)
        self.assertEqual(result, True)
        self.assertEqual(slist.size(), 0)


if __name__ == '__main__':

    unittest.main()