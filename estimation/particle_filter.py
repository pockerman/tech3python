"""
Implementation of Particle Filtering
"""

import numpy as np
import copy

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

    def __init__(self, state_vec,   mat_desc=PFMatrixDescription()):

        IterativeFilterBase.__init__(self, state_vec=state_vec)

        self._mat_desc = mat_desc
        self._particles = None
        self._weights = None
        self._importance_weight_calculator=None
        self._covariance_calculator = None
        self._predictor = None
        self._updater = None

    def initialize_paricles(self, initializer):

        """
        Initialize the particles of the filter using the given initializer
        :param initializer:
        :return:
        """
        self._particles = initializer

    def initialize_weights(self, weights_initializer):
        """
        Initialize the weights
        :param weights_initializer:
        :return:
        """
        self._weights = weights_initializer

    def set_predictor(self, predictor):
        """
        Set the object that will be used for predicting the particles state
        :param predictor:
        :return:
        """
        self._predictor = predictor

    def set_updater(self, updater):
        """
        Set the object that will be used for predicting the particles state
        :param predictor:
        :return:
        """
        self._updater = updater

    def set_importance_weights_calculator(self, calculator):
        """
        Set the type responsible for calculating the weights
        """
        self._importance_weight_calculator = calculator

    def set_covariance_calculator(self, calculator):
        """
        Set the type responsible for calculating the covariance matrix
        """
        self._covariance_calculator = calculator

    def get_particles(self):
        """
        Returns the particles list
        """
        return self._particles

    def set_matrix(self, name, mat):

        """
        Set the matrix named by the given name
        :param name: The name of the matrix to set
        :param mat:  The value to set the matrix to
        """
        self._mat_desc.set_matrix(name=name, item=mat)

    def get_matrix(self, name):
        """
        Returns the matrix with the given name
        """
        return self._mat_desc.get_matrix(name=name)

    def get_matrix_descriptor(self):
        """
        Returns the matrix descriptort object
        """
        return self._mat_desc

    def set_weights(self, weights):
        """
        Set the weights for the particles
        TODO: We should check if the given type is Numpy array and if not convert it
        """

        if isinstance(weights, type(self._weights)) == False:
            self._weights = np.array(shape=(len(weights), 1), dtype='float')

        self._weights = weights

    def get_weights(self):
        """
        Returns the weights for the particles
        """
        return self._weights

    def normalize_weights(self, **kwargs):
        """
        Normalize the weights
        """
        self._weights = self._weights/self._weights.sum() #sum(self._weights)

    def predict(self, **kwargs):

        self._particles = self._predictor(self._particles, **kwargs)

    def update(self, **kwargs):

        """
        Update the estimate. Essentially performs the resampling step
        meaning that a new set of particles and particle weights is generated
        """
        self._weights = self._updater(self._particles, self._weights, **kwargs)

    def iterate(self, **kwargs):
        """
        Perform own iteration over the steps fo PF
        """

        copy_kwargs = copy.deepcopy(kwargs)
        copy_kwargs['state'] = self.state

        self.predict(**copy_kwargs)
        self.update(**copy_kwargs)

        # update the state vector
        self.previous_state_vector = self.state
        self._mat_desc.update(**copy_kwargs)