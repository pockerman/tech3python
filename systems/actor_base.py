import copy
from abc import ABC
from abc import abstractmethod


class ActorBase(ABC):

    def __init__(self, **properties):

        self._properties = None
        if properties is not None:
            self._properties = copy.deepcopy(properties)

    @property
    def properties(self):
        return self._properties


    @abstractmethod
    def execute(self, **input):
        pass

    def __call__(self, **input):
        self.execute(**input)