
from .actor_base import ActorBase
class Adder(ActorBase):

    def __init__(self, a = 1, b = 1):
        ActorBase.__init__(self, {"a": a, "b": b})

    def execute(self, **input):

        a = self.properties["a"]
        b = self.properties["b"]
        return input["x1"]*a + input["x2"]*b