"""
Author:  Owen Fitzgerald
Purpose: Projectile motion calculation and plotting.
         With and without air resistance.
         Now with lagrange interpolation.

         Homework 2, Computational Physics 

Bugs:    If you give use certain strange values to the height it crashes.
         Tau can't be too small. 

Notes:   I like using list comprehensions more than np arrays. I don't know why.
         I modified the program a little since I took the screenshots for the questions,
         because I ended up obsessing over how best to write the interpolateTheoretical function.
         If you understand the three list comprehensions in interpolateTheoretical then then
         you understand pretty much all of what the interpolation is meant to do. 
"""

import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

def main():
    #* Set initial position and velocity of the baseball
    y0 = eval(input('Enter initial height (meters): '))
    r0 = np.array([0, y0])      # Initial vector position
    speed = eval(input('Enter initial speed (m/s): '))
    theta = eval(input('Enter initial angle (degrees): '))
    v0 = np.array([speed * np.cos(theta*np.pi/180), 
          speed * np.sin(theta*np.pi/180)])      # Initial velocity
    r = np.copy(r0)   # Set initial position 
    v = np.copy(v0)   # Set initial velocity

    #* Set physical parameters (mass, Cd, etc.)
    Cd = 0.35      # Drag coefficient (dimensionless)
    area = 4.3e-3  # Cross-sectional area of projectile (m^2)
    grav = 9.81    # Gravitational acceleration (m/s^2)
    mass = 0.145   # Mass of projectile (kg)
    airFlag = eval(input('Air resistance? (Yes:1, No:0): '))

    if airFlag == 0 :
        rho = 0.      # No air resistance
    else:
        rho = 1.2     # Density of air (kg/m^3)
    air_const = -0.5*Cd*rho*area/mass   # Air resistance constant

    #* Set physical parameters (mass, Cd, etc.)
    Cd = 0.35      # Drag coefficient (dimensionless)
    area = 4.3e-3  # Cross-sectional area of projectile (m^2)
    grav = 9.81    # Gravitational acceleration (m/s^2)
    mass = 0.145   # Mass of projectile (kg)

    tau = eval(input('Enter timestep, tau (sec): '))   # (sec)
    maxstep = 1000 # Maximum number of steps
    xplot = np.empty(maxstep)
    yplot = np.empty(maxstep)
    xNoAir = np.empty(maxstep)
    yNoAir = np.empty(maxstep)

    for istep in range(maxstep):
        #* Record position (computed and theoretical) for plotting
        xplot[istep] = r[0]   # Record trajectory for plot
        yplot[istep] = r[1]
        t = istep*tau         # Current time
        xNoAir[istep] = r0[0] + v0[0]*t
        yNoAir[istep] = r0[1] + v0[1]*t - 0.5*grav*t**2
        
        #* Calculate the acceleration of the ball 
        accel = air_const * np.linalg.norm(v) * v   # Air resistance
        accel[1] = accel[1] - grav                  # Gravity
      
        #* Calculate the new position and velocity using Euler method
        r = r + tau*v                    # Euler step                   
        v = v + tau*accel     

        #* If ball reaches ground (y<0), break out of the loop
        if r[1] < 0 : 
            laststep = istep+1
            xplot[laststep] = r[0]  
            yplot[laststep] = r[1]
            break

    print('Maximum range is', r[0], 'meters')
    print('Time of flight is', laststep*tau , ' seconds')

    #* Graph the trajectory of the baseball
    # Mark the location of the ground by a straight line
    xground = np.array([0., xNoAir[laststep-1]])
    yground = np.array([0., 0.])
    
    xInterpValues = interpolateTheoretical(xNoAir, yNoAir)[0] #x and y lists from interpolated theoretical values
    yInterpValues = interpolateTheoretical(xNoAir, yNoAir)[1]

    #For 3(c)
    print('The interpolated time of flight is '+ str(len(xInterpValues) * tau) + ' seconds') 
    print('The interpolated range is ' + str(xInterpValues[-1]) + ' meters')                                                                                             
    
    plt.plot(xplot[0:laststep+1], yplot[0:laststep+1], '+',
             xNoAir[0:laststep], yNoAir[0:laststep], '-',
             xInterpValues, yInterpValues,'-', #Added lagrange interpolation to plot
             xground, yground,'r-')

    plt.legend(['Euler method', 'Theory (No air)', 'Interpolation']);
    plt.xlabel('Range (m)')
    plt.ylabel('Height (m)')
    plt.title('Projectile motion')
    plt.show()

def interpolateTheoretical(xNoAir, yNoAir):
    xyTuples = [(xNoAir[i], yNoAir[i]) for i, y in enumerate(yNoAir) if y > 0 and i != 0] #(x,y), y > 0 except the start

    yInterpValues = [interpolate(xy[0], xyTuples[-3:]) for xy in xyTuples] #Interpolation from last 3 theoretical (x,y)
    xInterpValues = [xy[0] for i, xy in enumerate(xyTuples) if i < len(yInterpValues)] #Only x values used for interpolation
    
    return [xInterpValues, yInterpValues]

def interpolate(xi,xyInterpPairs): #xyInterpPair is a list of (x,y) pairs. 
    x = [xy[0] for xy in xyInterpPairs] 
    y = [xy[1] for xy in xyInterpPairs]
                         
    yi = ( (xi-x[1])*(xi-x[2])/((x[0]-x[1])*(x[0]-x[2])) * y[0]
    + (xi-x[0])*(xi-x[2])/((x[1]-x[0])*(x[1]-x[2])) * y[1]
    + (xi-x[0])*(xi-x[1])/((x[2]-x[0])*(x[2]-x[1])) * y[2])
    return yi

main()
