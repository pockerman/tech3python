"""
Kalaman Filter implementation
"""

import numpy as np
import functools


def check_in_matrices(matrix_names):
    def check_matrix_name_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):

            if kwargs.get('name') not in matrix_names:
                raise ValueError("Matrix name: " + kwargs.get('name') + " not in " + str(matrix_names))

            return f(*args, **kwargs)
        return wrapper
    return check_matrix_name_decorator


def check_not_none_matrix_decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs.get('mat') is None:
            raise ValueError("Cannot set a matrix to None. Need a value")
        return f(*args, **kwargs)
    return wrapper


class KFMatrixDescription:
    """
    Matrix description for Kalman Filter class
    """

    """
    Holds the names of the matrices used in the Kalaman Filter
    """
    NAMES = ["A", "B", "H", "P", "K", "Q", "R"]

    def __init__(self):
        self._matrices = dict()

    @check_in_matrices(NAMES)
    @check_not_none_matrix_decorator
    def set_matrix(self, name, mat):
        """
        Set the KF matrix name to the given value
        """
        self._matrices[name] = mat

    def __setitem__(self, key, value):
        self.set_matrix(name=key, mat=value)

    @check_in_matrices(NAMES)
    def get_matrix(self, name):
        return self._matrices[name]

    def __getitem__(self, item):
        self.get_matrix(name=item)

    def update(self, **input):
        """
        Performs any updates of the matrics if needed. Applications should
        provide the actual implementation
        """
        pass


class KalamanFilter:

    """
    Implementation of Kalman Filtering
    """

    def __init__(self, state_vec, mat_desc):
        self._state_vec = state_vec
        self._state_vec_prev = self._state_vec
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
        K = self._mat_desc["K"]
        K = P * H_T * S_inv

        innovation = z - H * self._state_vec
        self._state_vec += K * innovation
        I = np.identity(self._state_vec.shape)

        # update covariance matrix
        P = (I - K * H) * P

    def iterate(self, u, z, **kwrags):
        """
        Perform one iteration step for Kalman Filter
        """
        self.predict(u=u)
        self.update(z=z)
        self._mat_desc.update(kwrags)
