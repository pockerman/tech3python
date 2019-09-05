from base.basic_decorators import check_in_array
from base.basic_decorators import check_not_none


class MatrixDescription:
    """
    Matrix description for various filters
    """

    @classmethod
    def get_names(cls):
        raise NotImplementedError("Should be implemented by derived classes")

    def __init__(self):
        self._matrices = dict()
        self.initialize()

    def initialize(self):
        """
        Initialize the matrix descriptor
        """
        for name in self.get_names():
            self._matrices[name] = None

    @check_in_array(items=None)
    @check_not_none(msg="Cannot set a matrix to None. Need a value.")
    def set_matrix(self, name, item):
        """
        Set the Matrix with the given name to the given value
        """
        raise NotImplementedError("Should be implemented by derived classes")

    @check_in_array(items=None)
    def get_matrix(self, name):
        raise NotImplementedError("Should be implemented by derived classes")

    def update(self, **input):
        """
        Performs any updates of the matrices if needed. Applications should
        provide the actual implementation
        """
        pass

    def __getitem__(self, item):
        self.get_matrix(name=item)

    def __setitem__(self, key, value):
        self.set_matrix(name=key, mat=value)


