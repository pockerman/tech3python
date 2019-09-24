from .adt_base import ADTBase


class ArrayStack(ADTBase):

    """
    Basic array based stack implmentation
    """

    def __init__(self, capacity):
        ADTBase.__init__(self)
        self._size = 0
        self._capacity = capacity
        self._head_pos = -1
        self._data=[None for i in range(capacity)]

    def __len__(self):

        """
        Returns how many items are currently held in the stack
        """
        return self._size

    def capacity(self):

        """
        Returns the capacity of the stack
        """
        return self._capacity

    def push(self, value):

        """
        Push a new value at the top of the stack
        """

        if len(self)>= self.capacity():
            raise ValueError("Stack capacity has been reached")

        self._head_pos +=1
        self._data[self._head_pos] = value
        self._size += 1

    def pop(self):

        """
        Pop the top of the stack
        """

        if self.empty():
            raise ValueError("Empty Stack")

        data = self._data[self._head_pos]
        self._data[self._head_pos] = None
        self._head_pos -= 1
        self._size -= 1

        return data
