from abc import ABC
from abc import abstractmethod


class VehicleBase(ABC):
    """
    Base class for modeling a vehicle
    """

    def __init__(self, state, properties):

        self._state = state

        if properties is None:
            self.__properties = dict()
            self.__properties['mass'] = 0.0
        else:
            self.__properties = properties

    def get_property(self, name):
        return self.__properties[name]

    def set_property(self, name, value):
        self.__properties[name] = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

