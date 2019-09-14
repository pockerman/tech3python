"""
Motion model
"""


class MotionModel:
    """
    Vanilla motion model
    """

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        """
        :param args: args[0] = previous state vector, args[1] = system matrix A, args[2] = control matrix B, args[3] = control vector u
        """
        return args[1].dot(args[0]) + args[2].dot(args[3])
