"""
Category: Estimation, Filtering
ID: Example 5
Description: Localization using Particle Filter
Taken From: Kalman and Bayesian Filters in Python
https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python

"""


import numpy as np
from numpy.random import uniform
import scipy
import matplotlib.pyplot as plt
import math
import json

from estimation.particle_filter import ParticleFilter
from systems.system_state import SysState


def create_uniform_particles(size, x_range, y_range, hdg_range):

    particles = np.empty((size, 3))
    particles[:, 0] = uniform(x_range[0], x_range[1], size=size)
    particles[:, 1] = uniform(y_range[0], y_range[1], size=size)
    particles[:, 2] = uniform(hdg_range[0], hdg_range[1], size=size)
    particles[:, 2] %=  2*np.pi
    return particles

def create_gaussian_particles(mean, std, size):

    particles = np.empty((size, 3))
    particles[:, 0] = mean[0] + (np.random.randn(size) * std[0])
    particles[:, 1] = mean[1] + (np.random.randn(size) * std[1])
    particles[:, 2] = mean[2] + (np.random.randn(size) * std[2])
    particles[:, 2] %= 2 * np.pi
    return particles

def create_uniform_weights(size):
    weights = np.empty((size, 3))
    weights[:, 0] = uniform(1.0, 1.0, size=size)
    weights[:, 1] = uniform(1.0, 1.0, size=size)
    weights[:, 2] = uniform(1.0, 1.0, size=size)


def randomize_control_input(u, std, dt, size ):
    """
    Add noise to the given input
    """
    u[0] = u[0] + (np.random.randn() * std[0])
    u[1] = (u[1] * dt) + (np.random.randn() * std[1])

    return u


def predictor(particles, **kwargs):
    u = kwargs['u']
    particles[:, 2] += u[0]
    particles[:, 2] %= 2 * np.pi

    # move in the (noisy) commanded direction
    dist = u[1]
    particles[:, 0] += np.cos(particles[:, 2]) * dist
    particles[:, 1] += np.sin(particles[:, 2]) * dist
    return particles

def updater(particles, weights, **kwargs):
    weights.fill(1.)
    landmarks = kwargs['landmarks']
    z = kwargs['z']
    R = kwargs['R']
    for i, landmark in enumerate(landmarks):
        distance = np.linalg.norm(particles[:, 0:2] - landmark, axis=1)
        weights *= scipy.stats.norm(distance, R).pdf(z[i])
    weights += 1.e-300
    # avoid round-off to zero
    weights /= sum(weights)  # normalize
    return weights


def estimate(data):

    x_est = SysState(entries={"x": 0, "y": 1, "theta": 2})
    x_true = SysState(entries={"x": 0, "y": 1, "theta": 2})
    filter = ParticleFilter(state_vec=x_est)

    if data["PARTICLE_INITIALIZER"] == "Uniform":
        particle_initializer = create_uniform_particles(size=data["NUM_PARTICLES"], x_range=(0, 1 ), y_range=(0, 1), hdg_range=(0, np.pi*2))
        filter.initialize_paricles(initializer=particle_initializer)
    elif data["PARTICLE_INITIALIZER"] == "Gaussian":
        particle_initializer = create_uniform_particles(size=data["NUM_PARTICLES"], mean=data["MEAN"], std=math.sqrt(data["SIGMA"]))
        filter.initialize_paricles(initializer=particle_initializer)

    # initialize uniformly the weights
    weights = create_uniform_weights(size=data["NUM_PARTICLES"])
    filter.set_weights(weights=weights)

    u = np.array([0.0, 0.0])

    filter.set_predictor(predictor = predictor )
    filter.set_updater(updater=updater)

    kwargs=dict()
    time = 0.0
    for step in range(data["STEPS"]):
        time += data["DT"]
        print("\t At step: ", step+1, " of: ", data["STEPS"], "time is: ", time)

        kwargs["u"] = randomize_control_input(u=u, dt=data["DT"], size=data["NUM_PARTICLES"], std=(1.0, 1.0))
        filter.predict(**kwargs)

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
