"""
Measurement model
"""


class MeasurementModel:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        """
        :param args: args[0] = previous state vector, args[1] = matrix H
        """
        return args[1]*args[0]
