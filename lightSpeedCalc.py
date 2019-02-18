import math
from math import sqrt
import numpy as np

#Measurements from class.
#(Distance, time) in meters and seconds. 
measurements = [(3.316, 12 * 10**-9),
                (3.096, 10 * 10**-9),
                (3.506, 11 * 10**-9),
                (3.304, 11 * 10**-9)] 

#Uncertainty from measurements. 
dUncertainty = 10**-3
tUncertainty = 10**-9

#Finds each measurement's c value and uncertainty
cValues = []
cUncertainties = []
for measurement in measurements:
    d = measurement[0]
    t = measurement[1]
    c = d/t
    cValues.append(c)

    cUncertainty =  t ** -1 * sqrt(dUncertainty**2 + ((d *  tUncertainty) / t )**2) 
    cUncertainties.append(cUncertainty)

print('Speed of light values from measurements: ')
for cValue in cValues:
    print('{:.1e}'.format(cValue))
print()

print('Uncertainty in c from measuremnts: ')
for cUncertainty in cUncertainties:
    print('{:.0e}'.format(cUncertainty)) # 1 sig fig puts this on the same order as c. 
print()

#Final calculations. 
c = np.average(cValues)
cUncertainty = np.average(cUncertainties)

print('Final c calculation:')
print('{:.1e}'.format(c))
print()
print('Final uncertainty calculation:')
print('{:.0e}'.format(cUncertainty))


