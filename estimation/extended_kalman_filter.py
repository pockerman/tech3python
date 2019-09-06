"""
Implementation of Extended Kalman Filter algorithm
"""

import numpy as np

from base.basic_decorators import check_in_array
from base.basic_decorators import check_not_none
from .matrix_descriptor import MatrixDescription


class EKFMatrixDescription(MatrixDescription):
    """
    Matrix description for Extended Kalman Filter class
    """

    @classmethod
    def get_names(cls):
        return cls.NAMES

    """
    Holds the names of the matrices used in the Kalaman Filter
    """
    NAMES = ["A", "B", "H", "Hjac", "P", "K", "Q", "R", "L", "F"]

    def __init__(self):
        MatrixDescription.__init__(self)

    @check_in_array(items=NAMES)
    @check_not_none(msg="Cannot set a matrix to None. Need a value.")
    def set_matrix(self, name, mat):
        """
        Set the EKF matrix name to the given value
        """
        self._matrices[name] = mat

    @check_in_array(items=NAMES)
    def get_matrix(self, name):
        return self._matrices[name]


class ExtendedKalmanFilter:
    """
    Implementation of the Extended Kalman Filter algorithm
    """

    def __init__(self, state_vec, mat_desc, motion_model, measurement_model):
        self._state_vec = state_vec
        self._state_vec_prev = self._state_vec
        self._mat_desc = mat_desc
        self._motion_model = motion_model
        self._measurement_model = measurement_model

    def predict(self, u):
        """
        Performs the prediction step for Extended Kalman Filter
        """

        A = self._mat_desc["A"]
        B = self._mat_desc["B"]

        # update the prediction of the state vector
        self._state_vec = self._motion_model(self._state_vec_prev, A, B, u)

        P = self._mat_desc["P"]
        Q = self._mat_desc["Q"]
        L = self._mat_desc["L"]
        L_T = L.T
        F = self._mat_desc["F"]
        F_T = F.T
        P = F * P * F_T + L * Q * L_T
        self._mat_desc["P"] = P

    def update(self, z):
        """
        Performs the update step of the Kalman Filter
        """

        Hjac = self._mat_desc["Hjac"]
        H = self._mat_desc["H"];
        zpred = self._measurement_model(self._state_vec_prev , H)

        innovation = z - zpred
        P = self._mat_desc["P"]
        Hjac_T =  Hjac.T
        R = self._mat_desc["R"]
        M = self._mat_desc["M"]
        M_T = M.T
        S = Hjac * P * Hjac_T + M * R * M_T
        S_inv = np.linalg.inv(S)
        self._mat_desc["K"] = P * Hjac_T * S_inv
        self._state_vec += self._mat_desc["K"] * innovation
        I = np.identity(self._state_vec.shape)

        # update the covariance matrix
        P = (I - self._mat_desc["K"] * Hjac) * P
        self._mat_desc["P"] = P

    def iterate(self, u, z, **kwrags):
        """
        Perform one iteration step for Extended Kalman Filter
        """
        self.predict(u=u)
        self.update(z=z)
        self._mat_desc.update(kwrags)