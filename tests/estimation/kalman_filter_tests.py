"""
Unit tests for Kalman Filter class
"""

import unittest

from estimation.kalman_filter import KFMatrixDescription
from estimation.kalman_filter import KalamanFilter


class KalmanFilterTest(unittest.TestCase):

    """
    Test Scenario: Application attempts to set a matrix with a name not in the matrix name lists
    Expected Output: ValueError exception is raised
    """
    def test_invalid_matrix_name(self):
        kf_description = KFMatrixDescription()
        with self.assertRaises(ValueError) as context:
            kf_description.set_matrix(name="INVALID_NAME", mat=[0,1])

    """
    Test Scenario: Application attempts to set a matrix with a valid name as None
    Expected Output: ValueError exception is raised
    """
    def test_none_matrix(self):
        kf_description = KFMatrixDescription()
        with self.assertRaises(ValueError) as context:
            kf_description.set_matrix(name=KFMatrixDescription.NAMES[0], mat=None)


if __name__ == '__main__':
    unittest.main()