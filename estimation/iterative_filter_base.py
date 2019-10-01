"""
Base class for filtering algorithms
"""

from abc import abstractmethod
from abc import ABC

class IterativeFilterBase(ABC):

    """
    Base class for deriving iterative filters like Kalman Filter and Extended Kalman Filter
    """

    def __init__(self, state_vec):
        self._state = state_vec
        self._state_vec_prev = self._state

    @property
    def state(self):
        """
        Returns the state vector
        """
        return self._state

    @state.setter
    def state(self, value):
        """
        Returns the state vector
        """
        self._state = value

    @property
    def previous_state_vector(self):
        """
        Returns the previous state vector
        """
        return self._state_vec_prev

    @previous_state_vector.setter
    def previous_state_vector(self, value):
        self._state_vec_prev = value

    @abstractmethod
    def iterate(self, u, z, **kwargs):
        """
        Do one iteration step for the filter
        """
        raise NotImplementedError("Should be implemented by derived classes")

