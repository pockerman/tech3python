"""
Unit tests for ArrayStack
"""

import unittest

from adt.array_stack import ArrayStack


class TestArrayStack(unittest.TestCase):
    """
    Unit Test implementations for ArrayStack
    """

    """
    Test Scenario: Application creates an empty stack
    Expected Output: An empty stack should be returned to the application
    """

    def test_empty_stack_creation(self):
        stack = ArrayStack (capacity=100)
        self.assertTrue(stack.empty())

    """
    Test Scenario: Application creates an empty stack and tries to access the head element
    Expected Output: An IllegalStateException should be thrown
    """

    def test_empty_stack_pop_operation(self):
        stack = ArrayStack(capacity=100)
        with self.assertRaises(ValueError):
            stack.pop()

    """
    Test Scenario: Application creates an empty stack and adds one element.
                   It then tries to access the head element
    Expected Output: The head element should be returned
    """

    def test_stack_pop_operation(self):
        stack = ArrayStack(capacity=100)
        stack.push(10)
        head = stack.pop()
        self.assertEquals(head, 10, msg="Invalid head value")
        self.assertTrue(stack.empty())

    """
    Test Scenario: Application creates an empty stack and adds multiple elements.
                   It then tries to access the head element
    Expected Output: The head element should be returned
    """

    def test_stack_pop_operation_multiple_pushes(self):
        stack = ArrayStack(capacity=100)

        for i in range(stack.capacity()):
            stack.push(i)

        head = stack.pop()
        self.assertEquals(head, 99)

    """
    Test Scenario: Application creates an empty stack with a given capacity.
                   It then fully populates (i.e. exhaust the stack capacity) the stack. 
                   It then attempts to add one more element
    Expected Output: Element that exceeds the stack capacity should not be added. ValueError should be raise
    """

    def test_stack_full_push_operation(self):

        stack = ArrayStack(capacity=100)

        for i in range(stack.capacity()):
            stack.push(i)

        self.assertEqual(len(stack), stack.capacity())
        with self.assertRaises(ValueError):
            stack.push(100)
        self.assertEqual(len(stack), stack.capacity())


if __name__ == '__main__':

    unittest.main()