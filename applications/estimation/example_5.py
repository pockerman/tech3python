"""
Category: Estimation, Filtering
ID: Example 5
Description: Localization using Particle Filter
Taken From: Kalman and Bayesian Filters in Python
https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python

"""


import numpy as np
from numpy.random import uniform
import matplotlib.pyplot as plt
import math
import json

from estimation.particle_filter import ParticleFilter
from estimation.particle_filter import PFMatrixDescription
from systems.system_state import SysState
from estimation.motion_model import MotionModel
from estimation.measurement_model import MeasurementModel
from statistics.likelihood_models import GaussianModel


def create_uniform_particles(size, x_range, y_range, hdg_range):

    particles = np.empty((size, 3))
    particles[:, 0] = uniform(x_range[0], x_range[1], size=size)
    particles[:, 1] = uniform(y_range[0], y_range[1], size=size)
    particles[:, 2] = uniform(hdg_range[0], hdg_range[1], size=size)
    particles[:, 2] %=  2*np.pi
    return particles

def create_gaussian_particles(mean, std, size):

    particles = np.empty((size, 3))
    particles[:, 0] = mean[0] + (math.randn(size) * std[0])
    particles[:, 1] = mean[1] + (math.randn(size) * std[1])
    particles[:, 2] = mean[2] + (math.randn(size) * std[2])
    particles[:, 2] %= 2 * np.pi
    return particles


def randomize_control_input(u, std, dt, size ):
    """
    Add noise to the given input
    """
    u[0] = u[0] + (math.randn(size) * std[0])
    u[1] = (u[1] * dt) + (math.randn(size) * std[1])

    return u


def estimate(data):

    if data["PARTICLE_INITIALIZER"] == "Uniform":
        particle_initializer = create_uniform_particles(size=data["NUM_PARTICLES"], x_range=(0, 1 ), y_range=(0, 1), hdg_range=(0, np.pi*2))
    elif data["PARTICLE_INITIALIZER"] == "Gaussian":
        particle_initializer = create_uniform_particles(size=data["NUM_PARTICLES"], mean=data["MEAN"], std=math.sqrt(data["SIGMA"]))

    x_est = SysState(entries={"x":0, "y":1, "theta":2})
    x_true = SysState(entries={"x":0, "y":1, "theta":2})

    u = np.array([[0.0, 0.0]]).T

    filter = ParticleFilter(state_vec=x_est)
    filter.initialize_paricles(initializer=particle_initializer)

    kwargs=dict()
    time = 0.0
    for step in range(data["STEPS"]):
        time += data["DT"]
        print("\t At step: ", step+1, " of: ", data["STEPS"], "time is: ", time)

        kwargs["u"] = randomize_control_input(u=u, dt=data["DT"], size=data["NUM_PARTICLES"], std=(1.0, 1.0))
        filter.predict(**kwargs)

        #print("\t True state vector is: ", x_true)

        #filter.iterate(**{"DT":data["DT"], 'u': u, 'z': z})
        #x_est = filter.state

        #print("\t state vector is: ", x_est)


def main():
    with open("particle_filtering_data_5.json", 'r') as f:
        data = json.load(f)
        estimate(data)

if __name__ == '__main__':
    print("=======================================")
    print("Running Example  estimation/example_5")
    main()
    print("Done...")
    print("=======================================")
