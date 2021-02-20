from abc import abstractmethod
from .actor_base import ActorBase

class IntegratorBase(ActorBase):

    @staticmethod
    @abstractmethod
    def create(**kwargs):
        raise ValueError("Should be implemented by derived classes")

    @staticmethod
    @abstractmethod
    def type():
        raise ValueError("Should be implemented by derived classes")

    def __init__(self, **properties):
        ActorBase.__init__(self, **properties)

    @property
    def history_size(self):
        return len(self.properties["history"])

    @property
    def step_size(self):
        return self.properties["step_size"]

    @property
    def rhs_func(self):
        return self.properties["rhs_func"]

    def has_rhs_func(self):
        return "rhs_func" in self.properties.keys() and self.properties["rhs_func"] is not None

    def update_history(self, idx, value):

        if idx >= len(self.properties["history"]) or idx < 0:
                raise ValueError("Invalid hystory index. Index {0} not in [0, {1})".format(idx, len(self.properties["history"])))

        if value is not None:
            self.properties["history"][idx] = value
        else:
            raise ValueError("Attemp to set history value to None")

    def get_history(self, idx):

        history = self.properties["history"]
        if idx >= len(history) or idx < 0:
            raise ValueError("Invalid hystory index. Index %s not in [0, %s)" % (idx, self.__history_size))
        return history[idx]