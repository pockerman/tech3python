"""
Category: Quantum Computing
ID: Example 1
Description: Hello World with  ```Qiskit```
Taken From: Introduction to Coding Quantum Algorithms: A Tutorial Series Using Qiskit


Details:

"""

import numpy as np

from qiskit import ClassicalRegister
from qiskit import QuantumRegister
from qiskit import QuantumCircuit
from qiskit import execute
from qiskit import Aer


def main():

    S_simulator = Aer.backends(name="statevector_simulator")[0]
    M_simulator = Aer.backends(name="qasm_simulator")[0]

    q = QuantumRegister(1)
    hello_qubit = QuantumCircuit(q)

    # apply identity gate
    hello_qubit.iden(q[0])

    job = execute(hello_qubit, S_simulator)
    result = job.result()
    print("Result is: ", result.get_statevector())

if __name__ == '__main__':
    print("Running Example quantum_computing/example_1")
    main()
    print("Done...")