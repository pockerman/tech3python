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

    def __init__(self, num_particles, num_resample_particles, state_vec,  motion_model,
                 measurement_model, mat_desc=PFMatrixDescription()):

        IterativeFilterBase.__init__(self, state_vec=state_vec)

        self._num_particles = num_particles
        self._num_resample_particles = num_resample_particles
        self._motion_model = motion_model
        self._measurement_model = measurement_model
        self._mat_desc = mat_desc
        self._particles = np.zeros(shape=(state_vec.shape[0], num_particles), dtype='float')
        self._weights = np.zeros(shape=(1, num_particles), dtype='float')
        self._importance_weight_calculator=None
        self._covariance_calculator = None

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

        u = kwargs['u']

        for pidx in range(self._num_particles):

            # get the particle weight
            wp = self._weights[0, pidx]

            # calculate state vector from motion model
            state_vec = self._motion_model(self.previous_state_vector, self._mat_desc["F"], self._mat_desc["B"], u)

            kwargs['state'] = state_vec
            wp = self._importance_weight_calculator(wp, **kwargs)
            self._particles[:, pidx] = state_vec[:, 0]
            self._weights[0, pidx] = wp

        self.normalize_weights(**kwargs)

        state_vec = self._particles.dot(self._weights.T)
        self._mat_desc["P"] = self._covariance_calculator(state_vec, self._particles, self._weights)
        self.state = state_vec

    def update(self, **kwargs):

        """
        Update the estimate. Essentially performs the resampling step
        meaning that a new set of particles and particle weights is generated
        """

        Neff = 1.0 / (self._weights.dot(self._weights.T))[0, 0]  # Effective particle number
        NP = self._num_particles
        NTh = self._num_resample_particles

        if Neff < NTh:
            wcum = np.cumsum(self._weights)
            base = np.cumsum(self._weights * 0.0 + 1 / NP) - 1 / NP
            resampleid = base + np.random.rand(base.shape[0]) / NP

            inds = []
            ind = 0
            for ip in range(NP):
                while resampleid[ip] > wcum[ind]:
                    ind += 1
                inds.append(ind)

            self._particles = self._particles[:, inds]
            self._weights = np.zeros((1, NP)) + 1.0 / NP  # init weight

    def iterate(self, **kwargs):
        """
        Perform own iteration over the steps fo PF
        """

        copy_kwargs = copy.deepcopy(kwargs)
        copy_kwargs['state'] = self.state

        self.predict(**copy_kwargs)
        #self.update(**copy_kwargs)

        # update the state vector
        self.previous_state_vector = self.state
        self._mat_desc.update(**copy_kwargs)