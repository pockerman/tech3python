"""
Simple example demonstrating Particle Filtering.
The example is taking from: https://github.com/AtsushiSakai/PythonRobotics
https://github.com/AtsushiSakai/PythonRobotics/blob/master/Localization/particle_filter/particle_filter.py
"""

import numpy as np
import math
import json

from estimation.particle_filter import ParticleFilter
from estimation.particle_filter import PFMatrixDescription
from estimation.motion_model import MotionModel
from estimation.measurement_model import MeasurementModel
from statistics.likelihood_models import GaussianModel

Q = np.diag([0.1])**2  # range error

#  Simulation parameter
Qsim = np.diag([0.2]) ** 2
Rsim = np.diag([1.0, np.deg2rad(30.0)]) ** 2

# RFID positions [x, y]
RFID = np.array([[10.0, 0.0], [10.0, 10.0],
                 [0.0, 15.0], [-5.0, 20.0]])


class MatrixDescriptor(PFMatrixDescription):
    """
    Descriptor for the matrices
    """
    def __init__(self, **input):
        PFMatrixDescription.__init__(self)
        self.update(**input)
        cov = np.zeros(shape=(3, 3))
        self.set_matrix(name="P", item=cov)

    def update(self, **input):
        """
        Performs any updates of the matrices if needed. Applications should
        provide the actual implementation
        """
        F = np.array([[1.0, 0, 0, 0],
                      [0, 1.0, 0, 0],
                      [0, 0, 1.0, 0],
                      [0, 0, 0, 0]])

        self.set_matrix(name="F", item=F)

        B = np.array([[input['DT'] * math.cos(input['state'][2, 0]), 0],
                      [input['DT'] * math.sin(input['state'][2, 0]), 0],
                      [0.0, input['DT']],
                      [1.0, 0.0]])

        self.set_matrix(name="B", item=B)


def calc_input():

    v = 1.0  # [m/s]
    yawrate = 0.1  # [rad/s]
    u = np.array([[v, yawrate]]).T
    return u


def randomize_input(u):

    ud1 = u[0, 0] + np.random.randn() * Rsim[0, 0]
    ud2 = u[1, 0] + np.random.randn() * Rsim[1, 1]
    ud = np.array([[ud1, ud2]]).T
    return ud


def calculate_importance_weight(w, **kwargs):
    """
    Calc Importance Weight
    """
    z = kwargs['z']
    x = kwargs['state']

    for i in range(len(z[:, 0])):
        dx = x[0, 0] - z[i, 1]
        dy = x[1, 0] - z[i, 2]
        prez = math.sqrt(dx ** 2 + dy ** 2)
        dz = prez - z[i, 0]
        likelihood = GaussianModel(mu=dz, sigma=math.sqrt(Q[0, 0]))
        w = w * likelihood()


def calculate_covariance(state_vec):
    cov = np.zeros(shape=(3, 3))

    for i in range(px.shape[1]):
        dx = (px[:, i] - xEst)[0:3]
        cov += pw[0, i] * dx.dot(dx.T)

    return cov

def observation():
    pass


def show_animation():
    pass


def estimate(data):

    state_vector = np.zeros(shape=(4, 1))
    filter = ParticleFilter(state_vec=state_vector,
                            num_particles=data["NUM_PARTICLES"],
                            num_resample_particles=data["NUM_RESAMPLE_PARTICLES"],
                            likelihood_model=GaussianModel(mu=data["MU"], sigma=data["SIGMA"]),
                            motion_model=MotionModel(),
                            measurement_model=MeasurementModel(),
                            mat_desc=MatrixDescriptor(**{"DT": data["DT"], "state":state_vector}))


    time = 0.0
    for step in range(data["STEPS"]):
        time += data["DT"]
        print("\t At step: ", step+1, " of: ", data["STEPS"], "time is: ", time)
        u = randomize_input(calc_input())
        z = observation()
        state = filter.get_state()
        filter.iterate(u=u, z=z, **{"DT":data["DT"],"state":state})

        if data["SHOW_ANIMATION"]:
            show_animation()


def main():

    print("=======================================")
    print("Running Particle Filtering example...")
    with open("particle_filtering_data.json", 'r') as f:
        data = json.load(f)
        estimate(data)
    print("Done...")
    print("=======================================")


if __name__ == '__main__':
    main()
