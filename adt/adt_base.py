"""
Minimal base abstract class fro deriving
ADT
"""

from abc import abstractmethod
from abc import ABC

class ADTBase(ABC):

    def __init__(self):
        """
        constructors empty
        """
        super(ADTBase, self).__init__()

    @abstractmethod
    def __len__(self):
        """
        Returns the number of elements present in the ADT
        """
        raise NotImplementedError("Should be implemented by derived classes")

    @abstractmethod
    def push(self, value):
        """
        Adds a new value in the ADT. Concrete classes specify
        where the push occurs
        """
        raise NotImplementedError("Should be implemented by derived classes")

    @abstractmethod
    def delete(self, value):

        """
        Removes the given value in the ADT if present. Returns True if successful otherwise
        returns False
        """
        raise NotImplementedError("Should be implemented by derived classes")

    def empty(self):
        """
        Returns true if the ADT is empty
        """
        return len(self) == 0




