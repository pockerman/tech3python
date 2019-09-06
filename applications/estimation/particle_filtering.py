"""
Simple example demonstrating Particle Filtering.
The example is taking from: https://github.com/AtsushiSakai/PythonRobotics
https://github.com/AtsushiSakai/PythonRobotics/blob/master/Localization/particle_filter/particle_filter.py
"""

import numpy as np
import json

from estimation.particle_filter import ParticleFilter
from estimation.motion_model import MotionModel

#  Simulation parameter
Qsim = np.diag([0.2]) ** 2
Rsim = np.diag([1.0, np.deg2rad(30.0)]) ** 2

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


def observation():
    pass


def show_animation():
    pass


def estimate(data):

    state_vector = np.zeros(4, 1)
    filter = ParticleFilter(state_vec=state_vector,
                            num_particles=data["NUM_PARTICLES"], num_resample_particles=data["NUM_RESAMPLE_PARTICLES"],
                            motion_model=MotionModel())

    time = 0.0
    for step in range(data["STEPS"]):
        time += data["DT"]
        print("\t At step: ", step, "time is: ", time)
        u = randomize_input(calc_input())
        z = observation()

        filter.iterate(u=u, z=z)

        if data["SHOW_ANIMATION"]:
            show_animation()


def main():

    print("=======================================")
    print("Running Particle Filtering example...")
    data = json.load("particle_filtering_data.json")
    estimate(data)
    print("Done...")
    print("=======================================")


if __name__ == '__main__':
    main()
