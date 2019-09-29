"""

Category: Estimation
ID: Example 1
Description: Localization using Particle Filter 
Taken From: https://github.com/AtsushiSakai/PythonRobotics
https://github.com/AtsushiSakai/PythonRobotics/blob/master/Localization/particle_filter/particle_filter.py
Dependencies NumPy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import json

from estimation.particle_filter import ParticleFilter
from estimation.particle_filter import PFMatrixDescription
from estimation.motion_model import MotionModel
from estimation.measurement_model import MeasurementModel
from statistics.likelihood_models import GaussianModel

Q = np.diag([0.1])**2  # range error
R = np.diag([1.0, np.deg2rad(40.0)])**2  # input error

#  Simulation parameter
Qsim = np.diag([0.2]) ** 2
Rsim = np.diag([1.0, np.deg2rad(30.0)]) ** 2


# RFID positions [x, y]
RFID = np.array([[10.0, 0.0], [10.0, 10.0],
                 [0.0, 15.0], [-5.0, 20.0]])

# maximum observation range
MAX_RANGE = 20.0


class MatrixDescriptor(PFMatrixDescription):
    """
    Descriptor for the matrices
    """
    def __init__(self, **input):
        PFMatrixDescription.__init__(self)
        self.update(**input)
        P = np.eye(4)
        self.set_matrix(name="P", item=P)

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

    """
    Add noise to the given input
    """
    ud1 = u[0, 0] + np.random.randn() * Rsim[0, 0]
    ud2 = u[1, 0] + np.random.randn() * Rsim[1, 1]
    ud = np.array([[ud1, ud2]]).T
    return ud


def calculate_importance_weight(w, **kwargs):

    """
    Calculate the importance weights
    """
    z = kwargs['z']
    x = kwargs['state']

    for i in range(len(z[:, 0])):
        dx = x[0, 0] - z[i, 1]
        dy = x[1, 0] - z[i, 2]
        prez = math.sqrt(dx ** 2 + dy ** 2)
        dz = prez - z[i, 0]
        likelihood = GaussianModel(mu=dz, sigma=math.sqrt(Q[0, 0])**2)
        w = w * likelihood()
    return w


def calculate_covariance(state_vec, particles, particle_weights):

    cov = np.zeros(shape=(3, 3))

    for i in range(particles.shape[1]):
        dx = (particles[:, i] - state_vec)[0:3]
        cov += particle_weights[0, i] * dx.dot(dx.T)
    return cov


def motion_model(x, u, mat_descriptor):

    F = mat_descriptor.get_matrix(name="F")
    B = mat_descriptor.get_matrix(name="B")
    return F.dot(x) + B.dot(u)


def observation(x_true, xd, u, matrix_descriptor):

    x_true = motion_model(x_true, u, matrix_descriptor)

    # add noise to gps x-y
    z = np.zeros((0, 3))

    for i in range(len(RFID[:, 0])):

        dx = x_true[0, 0] - RFID[i, 0]
        dy = x_true[1, 0] - RFID[i, 1]
        d = math.sqrt(dx ** 2 + dy ** 2)
        if d <= MAX_RANGE:
            dn = d + np.random.randn() * Qsim[0, 0]  # add noise
            zi = np.array([[dn, RFID[i, 0], RFID[i, 1]]])
            z = np.vstack((z, zi))

    # add noise to input
    ud = randomize_input(u)
    xd = motion_model(xd, ud, matrix_descriptor)
    return x_true, z, xd, ud


def plot_covariance_ellipse(x_est, P_est):  # pragma: no cover

    Pxy = P_est[0:2, 0:2]
    eigval, eigvec = np.linalg.eig(Pxy)

    if eigval[0] >= eigval[1]:
        bigind = 0
        smallind = 1
    else:
        bigind = 1
        smallind = 0

    t = np.arange(0, 2 * math.pi + 0.1, 0.1)

    # eigval[bigind] or eiqval[smallind] were occassionally negative numbers extremely
    # close to 0 (~10^-20), catch these cases and set the respective variable to 0
    try:
        a = math.sqrt(eigval[bigind])
    except ValueError:
        a = 0

    try:
        b = math.sqrt(eigval[smallind])
    except ValueError:
        b = 0

    x = [a * math.cos(it) for it in t]
    y = [b * math.sin(it) for it in t]
    angle = math.atan2(eigvec[bigind, 1], eigvec[bigind, 0])

    R = np.array([[math.cos(angle), math.sin(angle)],
                  [-math.sin(angle), math.cos(angle)]])

    fx = R.dot(np.array([[x, y]]))
    px = np.array(fx[0, :] + x_est[0, 0]).flatten()
    py = np.array(fx[1, :] + x_est[1, 0]).flatten()
    plt.plot(px, py, "--r")


def estimate(data):

    x_est = np.zeros(shape=(4, 1))
    x_true = np.zeros(shape=(4, 1))
    x_dr = np.zeros(shape=(4, 1))  # Dead reckoning

    # history
    hx_est = x_est
    hx_true = x_true
    hx_dr = x_true

    filter = ParticleFilter(state_vec=x_est,
                            num_particles=data["NUM_PARTICLES"],
                            num_resample_particles=data["NUM_RESAMPLE_PARTICLES"],
                            motion_model=MotionModel(),
                            measurement_model=MeasurementModel(),
                            mat_desc=MatrixDescriptor(**{"DT": data["DT"], "state":x_est}))

    # uniform initialization of the particle weights
    filter.set_weights(np.zeros(shape=(1, data["NUM_PARTICLES"]), dtype='float') + 1/data["NUM_PARTICLES"])

    # set the calculators for the weights and the covariance
    filter.set_importance_weights_calculator(calculator=calculate_importance_weight)
    filter.set_covariance_calculator(calculator=calculate_covariance)

    time = 0.0
    for step in range(data["STEPS"]):
        time += data["DT"]
        print("\t At step: ", step+1, " of: ", data["STEPS"], "time is: ", time)

        x_true, z, xd, u = observation(x_true=x_true, xd=x_dr, u=calc_input(), matrix_descriptor=filter.get_matrix_descriptor())

        print("\t True state vector is: ", x_true)

        filter.iterate(**{"DT":data["DT"], 'u': u, 'z': z})
        x_est = filter.state

        print("\t state vector is: ", x_est)

        if data["SHOW_ANIMATION"]:

            # store data history
            hx_est = np.hstack((hx_est, x_est))
            hx_dr = np.hstack((hx_dr, x_dr))
            hx_true = np.hstack((hx_true, x_true))

            particles = filter.get_particles()
            P = filter.get_matrix("P")

            plt.cla()

            for i in range(len(z[:, 0])):
                plt.plot([x_true[0, 0], z[i, 1]], [x_true[1, 0], z[i, 2]], "-k")

            plt.plot(RFID[:, 0], RFID[:, 1], "*k")
            plt.plot(particles[0, :], particles[1, :], ".r")

            plt.plot(np.array(hx_true[0, :]).flatten(), np.array(hx_true[1, :]).flatten(), "-b")
            plt.plot(np.array(hx_dr[0, :]).flatten(), np.array(hx_dr[1, :]).flatten(), "-k")
            plt.plot(np.array(hx_est[0, :]).flatten(), np.array(hx_est[1, :]).flatten(), "-r")

            plot_covariance_ellipse(x_est=x_est, P_est=P)
            plt.axis("equal")

            plt.grid(True)
            plt.pause(0.001)


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
