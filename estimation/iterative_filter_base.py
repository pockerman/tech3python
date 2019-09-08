"""
Base class for filtering algorithms
"""

from abc import abstractmethod
from abc import ABC

class IterativeFilterBase(ABC):

    def __init__(self, state_vec):
        self._state = state_vec
        self._state_vec_prev = self._state

    def get_state(self):
        """
        Returns the state vector
        """
        return self._state

    def get_previous_state_vector(self):
        """
        Returns the previous state vector
        """
        return self._state_vec_prev

    @abstractmethod
    def iterate(self, u, z, **kwargs):
        """
        Do one iteration step for the filter
        """
        raise NotImplementedError("Should be implemented by derived classes")

