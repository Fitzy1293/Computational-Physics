import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

r = [1, 1, 2, 2, 5] #Index + 1 to match the book. 
v = [2, 0, 5] #Second voltage will vary.

matrixA = np.array([[-1 * (r[0] + r[1]), 0, -1 * r[2]], #Matrix with no variables.
           [0, -1 * (r[3] + r[4]), -1 * r[2]],          #Use to solve for the three currents. 
           [1, 1, -1]])

voltages = []
powers = []

#Finds power delivered to R5 from V2 = 0 through 20.
for volts in range(21): 
    voltages.append(volts)

    matrixB = np.array([volts - v[0], volts - v[2], 0])

    mult = np.linalg.solve(matrixA, matrixB)

    power = abs(mult[1]**2 * r[4])

    powers.append(power)


plt.plot(voltages, powers)
plt.xlabel('Voltage from E2 (V)')
plt.ylabel('Power delivered to R5 (W)')
plt.show()

