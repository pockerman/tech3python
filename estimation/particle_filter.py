"""
Implementation of Particle Filtering
"""

import numpy as np

from base.basic_decorators import check_in_array
from base.basic_decorators import check_not_none
from .matrix_descriptor import MatrixDescription
from .iterative_filter_base import IterativeFilterBase


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
    def set_matrix(self, name, item):
        """
        Set the EKF matrix name to the given value
        """
        self._matrices[name] = item

    @check_in_array(items=NAMES)
    def get_matrix(self, name):
        return self._matrices[name]


class ParticleFilter(IterativeFilterBase):
    """
    Implements Particle Filter algorithm
    """

    def __init__(self, num_particles, num_resample_particles, state_vec,  motion_model,
                 measurement_model, likelihood_model, mat_desc=PFMatrixDescription()):

        IterativeFilterBase.__init__(self, state_vec=state_vec)

        self._num_particles = num_particles
        self._num_resample_particles = num_resample_particles
        self._motion_model = motion_model
        self._measurement_model = measurement_model
        self._likelihood_model = likelihood_model
        self._mat_desc = mat_desc
        self._weights = np.zeros(shape=(num_particles, 1), dtype='float')
        self._importance_weight_calculator=None
        self._calculate_covariance = None


    def set_importance_weights_calculator(self, calculator):
        self._importance_weight_calculator = calculator

    def set_weights(self, weights):
        """
        Set the weights for the particles
        TODO: We should check if the given type is Numpy array and if not convert it
        """

        if isinstance(weights, type(self._weights)) == False:
            self._weights = np.array(shape=(len(weights), 1), dtype='float')

        self._weights = weights

    def normalize_weights(self, **kwargs):
        """
        Normalize the weights
        """
        self._weights = self._weights/sum(self._weights)

    def calculate_importance_weight(self):
        pass

    def calculate_covariance(self, **kwargs):
        """
        Calculates the covariance matrix P
        """
        pass

    def predict(self, u, **kwargs):

        for pidx in range(self._num_particles):
            wp = self._weights[pidx]

            state_vec = self._motion_model(self.get_previous_state_vector(), self._mat_desc["F"], self._mat_desc["B"], u)
            kwargs['state'] = state_vec
            wp = self.calculate_importance_weight(wp, **kwargs)

            px[:, pidx] = state_vec[:, 0]
            pw[0, pidx] = wp

        self.normalize_weights(**kwargs)

        state_vec = px.dot(pw.T)
        self._mat_desc["P"] = self._calculate_covariance(state_vec, px, pw)

        self.calculate_covariance(**kwargs)

    def update(self, z, **kwargs):

        """
        Update the estimate. Essentially performs the resampling step
        """
        pass

    def iterate(self, u, z, **kwargs):
        self.predict(u=u, **kwargs)
        self.update(z=z, **kwargs)
        self._mat_desc.update(**kwargs)