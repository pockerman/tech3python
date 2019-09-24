"""
Simple implementation of a singly linked list

"""

from .adt_base import ADTBase

class SingleLinkedListNode(object):

    """
    The node of the list
    """

    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        self._next_node = value

    def __str__(self):
        """
        Return a string representation of the held data
        """
        return str(self._data)


class SinglyLinkedList(ADTBase):

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._n_elements = 0

    def size(self):
        return self._n_elements

    def __len__(self):
        return self.size()


    def push(self, value):
        """
        Adds a new value in the linked list.
        """
        if self._head is None:
            node = SingleLinkedListNode(data=value, next_node=self._tail)
            self._head = SingleLinkedListNode(data=None, next_node=node)
        else:

            # hold a reference to the next node
            next_node = self._head.next_node
            node = SingleLinkedListNode(data=value, next_node=next_node)
            self._head.next_node = node

        self._n_elements += 1
        return node

    def delete_node(self, node)->bool:
        """
        Delete the given node from the list.
        Returns true is done successfully otherwise returns false
        """

        if node is None or self._head is None:
            return False

        # else we need to find the node
        next_node = self._head.next_node
        previous_node = self._head

        found = False

        while(next_node is not None):

            if next_node == node:
                # we found the node to delete
                previous_node.next_node = next_node.next_node
                next_node = None
                node = None
                found = True
                self._n_elements -= 1
                break

            previous_node = next_node
            next_node = next_node.next_node

        return found

    def head(self):
        """
        Returns the top node that has valid data
        The _head node is initialized with None data
        """

        if self._head is None:
            return None

        return self._head.next_node

    def __str__(self):

        if self._head is None:
            return "Empty List"

        data = self._head.next_node.__str__() + ","
        next_n = self._head.next_node.next_node

        while (next_n is not None):

            data += next_n.__str__()
            next_n = next_n.next_node

            if next_n is not None:
                data += ","

        return data







    """
    slist = SinglyLinkedList()
    slist.add_head(value=3)

    print(slist.head())

    for i in range(10):
        slist.add_head(i)

    string = slist.__str__()
    print(string)
    """