"""
Implementation of Particle Filtering
"""

import numpy as np

from base.basic_decorators import check_in_array
from base.basic_decorators import check_not_none
from .matrix_descriptor import MatrixDescription


class PFMatrixDescription(MatrixDescription):
    """
    Matrix description for Particle Filter class
    """

    @classmethod
    def get_names(cls):
        return cls.NAMES

    """
    Holds the names of the matrices used in the Kalaman Filter
    """
    NAMES = ["A", "B", "P", "K", "Q", "R", "F"]

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


class ParticleFilter:
    """
    Implements Particle Filter algorithm
    """

    def __init__(self, num_particles, num_resample_particles, state_vec,  motion_model,
                 measurement_model, likelihood_model, mat_desc=PFMatrixDescription()):
        self._num_particles = num_particles
        self._num_resample_particles = num_resample_particles
        self._state_vec = state_vec
        self._state_vec_prev = self._state_vec
        self._motion_model = motion_model
        self._measurement_model = measurement_model
        self._likelihood_model = likelihood_model
        self._mat_desc = mat_desc
        self._weights = None

    def set_weights(self, weights):
        self._weights = weights

    def normalize_weights(self):
        self._weights = self._weights/sum(self._weights)

    def calculate_importance_weight(self):
        pass

    def calculate_covariance(self):
        """
        Calculates the covariance matrix P
        """
        pass

    def predict(self, u, **kwargs):

        for pidx in range(self._num_particles):
            wp = self._weights[pidx]
            self._state_vec = self._motion_model(self._state_vec_prev, self._mat_desc["F"], self._mat_desc["B"], u)

            self.calculate_importance_weight()

        self.normalize_weights()
        self.calculate_covariance()


    def update(self, z, **kwargs):

        """
        Update the estimate. Essentially performs the resampling step
        """
        pass


    def iterate(self, u, z, **kwargs):
        self.predict(u=u, **kwargs)
        self.update(z=z, **kwargs)