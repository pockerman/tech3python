from systems.integrator import IntegratorBase


class ODEScalarFWDEuler(IntegratorBase):

    @staticmethod
    def create(**kwargs):
        return ODEScalarFWDEuler(**kwargs)

    @staticmethod
    def type():
        return "SCALAR_FWD_EULER"

    def __init__(self, **kwargs):

        IntegratorBase.__init__(self, **kwargs)

        if 'init_condition' in kwargs.keys():
            self.update_history(0, kwargs['init_condition'] )

    def execute(self, **input):

        # get the callable to calculate the rhs
        if self.has_rhs_func():
            f = self.rhs_func
        elif 'f' in input.keys():
            f = input['f']
        else:
            raise ValueError("Right hand side function has not been defined")

        yn = self.get_history(0)
        new = yn + self.step_size*f(**input)
        yn = new
        self.update_history(0, yn)
        return new

class ODEVectorFWDEuler(IntegratorBase):

    @staticmethod
    def create(**kwargs):
        return ODEVectorFWDEuler(**kwargs)

    @staticmethod
    def type():
        return "VECTOR_FWD_EULER"

    def __init__(self, **kwargs):
        IntegratorBase.__init__(self, **kwargs)

        if 'init_condition' in kwargs.keys():
            self.update_history(0, kwargs['init_condition'] )

    def execute(self, **input):

        # get the callable to calculate the rhs
        if self.has_rhs_func():
            f = self.rhs_func
        elif 'f' in input.keys():
            f = input['f']
        else:
            raise ValueError("Right hand side function has not been defined")

        yn = self.get_history(0)
        new = yn + self.step_size*f(**input)
        yn = new
        self.update_history(0, yn)
        return new




