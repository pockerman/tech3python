import unittest

from estimation.matrix_descriptor import MatrixDescriptionIterator
from estimation.kalman_filter import KFMatrixDescription
from estimation.kalman_filter import KalmanFilter

class InvalidMockMatrixDescriptor:
    pass


class MatrixDescriptorsTest(unittest.TestCase):
    """
    Unit tests for matrix descriptors
    """

    """
    Test Scenario: Application attempts to initialize the MatrixDescriptionIterator
    with an instance that is not a subclass of MatrixDescription
    Expected Output: ValueError should be raised
    """
    def test_invalid_matrix_descriptor_given_to_matrix_iterator(self):

        mat_desc = InvalidMockMatrixDescriptor()
        with self.assertRaises(ValueError) as context:
            iterator = MatrixDescriptionIterator(matrix_descriptor=mat_desc)

    """
       Test Scenario: Application initializes the MatrixDescriptionIterator
       with a valid MatrixDescriptor 
       Expected Output: Valid iteration should be performed
    """
    def test_valid_matrix_descriptor_given_to_matrix_iterator(self):

        mat_desc = KFMatrixDescription()
        kf_names = mat_desc.get_names()

        iterator = MatrixDescriptionIterator(matrix_descriptor=mat_desc)
        counter = 0
        for name, mat in iterator:
            self.assertTrue(name in kf_names, msg="Name: "+name+" not in: "+str(kf_names))
            counter += 1

        self.assertEqual(counter, len(kf_names), msg=" Name counter: "+str(counter)+" not equal to: "+str(len(kf_names))+" Not all names iterated??")

if __name__ == '__main__':
    unittest.main()