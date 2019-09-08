"""
Kalaman Filter implementation
"""

import numpy as np

from .iterative_filter_base import IterativeFilterBase
from base.basic_decorators import check_in_array
from base.basic_decorators import check_not_none
from .matrix_descriptor import MatrixDescription


class KFMatrixDescription(MatrixDescription):
    """
    Matrix description for Kalman Filter class
    """

    @classmethod
    def get_names(cls):
        return cls.NAMES

    """
    Holds the names of the matrices used in the Kalman Filter class
    """
    NAMES = ["A", "B", "H", "P", "K", "Q", "R"]

    def __init__(self):
        MatrixDescription.__init__(self)

    @check_in_array(items=NAMES)
    @check_not_none(msg="Cannot set a matrix to None. Need a value.")
    def set_matrix(self, name, item):
        """
        Set the Matrix with the given name to the given value
        """
        self._matrices[name] = item

    @check_in_array(items=NAMES)
    def get_matrix(self, name):
        return self._matrices[name]


class KalmanFilter(IterativeFilterBase):

    """
    Implementation of Kalman Filtering
    """

    def __init__(self, state_vec, mat_desc):
        IterativeFilterBase.__init__(self, state_vec=state_vec)
        self._mat_desc = mat_desc

    def predict(self, u):
        """
        Performs the prediction step for Kalman Filter
        """
        self._state_vec = self._mat_desc["A"]*self._state_vec_prev + self._mat_desc["B"]*u
        a_t = self._mat_desc["A"].T
        self._mat_desc["P"] = self._mat_desc["A"]*self._mat_desc["P"]*a_t + self._mat_desc["Q"]

    def update(self, z):

        """
        Performs the update step of the Kalman Filter
        """

        H = self._mat_desc["H"]
        H_T = self._mat_desc["H"].T
        P = self._mat_desc["P"]
        R = self._mat_desc["R"]

        S = H * P * H_T + R
        S_inv = np.linalg.inv(S)

        # compute gain matrix
        self._mat_desc["K"] = P * H_T * S_inv

        innovation = z - H * self._state_vec
        self._state_vec += self._mat_desc["K"] * innovation
        I = np.identity(self._state_vec.shape)

        # update covariance matrix
        P = (I - self._mat_desc["K"] * H) * P
        self._mat_desc["P"] = P

    def iterate(self, u, z, **kwargs):
        """
        Perform one iteration step for Kalman Filter
        """
        self.predict(u=u)
        self.update(z=z)
        self._mat_desc.update(kwargs)
