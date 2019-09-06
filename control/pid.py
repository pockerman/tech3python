"""
PID controller implementation
"""

from base.basic_decorators import check_in_array
from base.basic_decorators import check_not_none


class PIDControl:
    """
    Simple implementation of PID controller
    """

    NAMES = ["Kp", "Ki", "Kd"]

    def __init__(self, Kp, Ki, Kd):
        self.__properties = dict()
        self.__error = 0.0

        if Kp is not None:
            self.set_property('Kp', Kp)

        if Ki is not None:
            self.set_property('Ki', Ki)

        if Kd is not None:
            self.set_property('Kd', Kd)

    def execute(self, error, **kwargs):

        rslt = 0.0

        if self.has_property('Kd') and 'dt' in kwargs.keys():
            delta_error = error - self.__error
            dt = kwargs['dt'] # what happens here if dt = 0.0
            rslt += self.get_property('Kd') * (delta_error/dt)

        if self.has_property('Kp'):
            rslt += self.get_property('Kp')*error

        # accumulate  the error
        self.__error += error

        if self.has_property('Ki'):
            rslt += self.get_property('Ki') * self.__error

        return rslt

    @check_in_array(items=NAMES)
    def get_property(self, name):
        return self.__properties[name]

    @check_in_array(items=NAMES)
    @check_not_none(msg="Cannot set property to None. Need a value.")
    def set_property(self, name, item):
        self.__properties[name] = item

    def has_property(self, name):
        return name in self.__properties.keys()

    def __getitem__(self, item):
        self.get_property(name=item)

    def __setitem__(self, key, value):
        self.set_property(name=key, item=value)

