"""
Implements common probability models
"""
import numpy as np


class GaussianModel:

    """
    Gaussian distribution
    """

    def __init__(self, mu=0.0, sigma=1.0):
        self._mu = mu
        self._sigma = sigma

    def __call__(self, *args, **kwargs):

        x=0.0
        if len(args) > 1: x = args[0]
        return np.random.normal(loc=(x-self._mu), scale=self._sigma)