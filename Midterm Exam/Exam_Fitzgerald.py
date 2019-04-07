# balle - Program to compute the trajectory of a baseball
#         using the Euler method.

# Set up configuration options and special features
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

#* Set initial position and velocity of the baseball
y0 = eval(input('Enter initial height (meters): '))   
r0 = np.array([0, y0])      # Initial vector position
speed = eval(input('Enter initial speed (m/s): '))
theta = eval(input('Enter initial angle (degrees): '))

v0 = np.array([speed * np.cos(theta*np.pi/180), 
      speed * np.sin(theta*np.pi/180)])      # Initial velocity
r = np.copy(r0)   # Set initial position 
v = np.copy(v0)   # Set initial velocity

# Arrays for interpolating
LastThreeX = np.array([])
LastThreeY = np.array([])

#Definition for interpolating
def intrpf(xi,x,y):
    """Function to interpolate between data points
       using Lagrange polynomial (quadratic)
       Inputs
        x    Vector of x coordinates of data points (3 values)
        y    Vector of y coordinates of data points (3 values)
        xi   The x value where interpolation is computed
      Output
        yi   The interpolation polynomial evaluated at xi
    """

    #* Calculate yi = p(xi) using Lagrange polynomial
    yi = ( (xi-x[1])*(xi-x[2])/((x[0]-x[1])*(x[0]-x[2])) * y[0]
    + (xi-x[0])*(xi-x[2])/((x[1]-x[0])*(x[1]-x[2])) * y[1]
    + (xi-x[0])*(xi-x[1])/((x[2]-x[0])*(x[2]-x[1])) * y[2] )
    return yi

def showPlots(vxAir, vyAir, vxNoAir, vyNoAir, xground, yground):
    #I got rid of the other plot as this exam asks for velocities. 
    #I used this website https://matplotlib.org/gallery/lines_bars_and_markers/spectrum_demo.html#sphx-glr-gallery-lines-bars-and-markers-spectrum-demo-py
    #As a template for plotting multiple plots at once. 
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(7, 7))

    #Plot the velocity components.
    axes[0, 0].legend(['Air resistance, x velocity',
                'Air resistance, y velocity',
               'No air resistance, x velocity',
                'No air resistance, y velocity'])

    axes[0, 0].plot(timeSteps, vxAir , 'r-', 
             timeSteps, vyAir, 'g-',
             timeSteps, vxNoAir , 'b-', 
             timeSteps, vyNoAir, 'y-')

    axes[0, 0].set_xlabel('Time (s)')
    axes[0, 0].set_ylabel('Velocity (m/s)')
    axes[0, 0].set_title('Velocity components as v(t) with and without air resistance.')

    #vxAir plot.
    axes[1, 0].plot(timeSteps, vxAir , 'r-')
    axes[1, 0].set_xlabel('Time (s)')
    axes[1, 0].set_ylabel('Velocity (m/s)')
    axes[1, 0].set_title('Air resistance: x component')

    #vyAir plot.
    axes[1, 1].plot(timeSteps, vyAir , 'g-')
    axes[1, 1].set_xlabel('Time (s)')
    axes[1, 1].set_ylabel('Velocity (m/s)')
    axes[1, 1].set_title('Air resistance: y component')

    #vxNoAir plot.
    axes[2, 0].plot(timeSteps, vxNoAir , 'b-')
    axes[2, 0].set_xlabel('Time (s)')
    axes[2, 0].set_ylabel('Velocity (m/s)')
    axes[2, 0].set_title('No air resistance: x component')

    #vyNoAir plot.
    axes[2, 1].plot(timeSteps, vyNoAir , 'y-')
    axes[2, 1].set_xlabel('Time (s)')
    axes[2, 1].set_ylabel('Velocity (m/s)')
    axes[2, 1].set_title('No air resistance: y component')


    axes[0, 1].legend(['Euler method', 'Theory (No air)', 'Interpolation'])

    axes[0, 1].plot(xplot[0:laststep+1],
                    yplot[0:laststep+1], '+',
             xNoAir[0:laststep], yNoAir[0:laststep], '-',
             xground, yground,'r-')

    axes[0, 1].set_xlabel('Range (m)')
    axes[0, 1].set_ylabel('Height (m)')
    axes[0, 1].set_title('Projectile motion')

    fig.tight_layout()
    plt.show()

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

#* Loop until ball hits ground or max steps completed
tau = eval(input('Enter timestep, tau (sec): '))   # (sec)
print()

maxstep = 1000    # Maximum number of steps
xplot = np.empty(maxstep);  yplot = np.empty(maxstep)
xNoAir = np.empty(maxstep); yNoAir = np.empty(maxstep)

#Getting a 2D list velocities (x,y components) air resistance and no air resistance.
#They all start with the same parameters, but change over time
vInit = [speed * np.cos(theta*np.pi/180), speed * np.sin(theta*np.pi/180)]
vAir = [vInit] 
vNoAir = [vInit]
timeSteps = [0] #Need to have the amount of time on x, because v is a function of x. 
               #Should be the same length as vAir and vNoAir

time = 0 #Add tau on for every iteration of maxstep. 
 #Initial y velocity to subtract grav from during the y


vyCurrent = vInit[1]

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

    #For plotting the velocities as a function of time. 
    #Adds current v to a list for plotting later.  

    vxCurrent = vInit[0] #x velocity is constant if there is no ar resistance. 

    vyCurrent = vyCurrent - (grav * tau) #Velocity minus acceleration due to gravity, kinematics. 
    vAir.append(list(v))
    
    vNoAir.append([vxCurrent, vyCurrent])
    
    time = time + tau #Get the time for the ball is at, use on x axis. 
    timeSteps.append(time)

  
    #* If ball reaches ground (y<0), break out of the loop
    if r[1] < 0 : 
        #Record how many times we go through the loop, which tells us 
        #how many points were calculated, needed for plotting the correct points 
        laststep = istep+1      
        xplot[laststep] = r[0]  # Record last values computed
        yplot[laststep] = r[1]

        #Record last three x- and y-points to use in interpoloation
        for i in range(0,3):
            LastThreeX =  np.append(LastThreeX, xplot[laststep - i])
            LastThreeY =  np.append(LastThreeY, yplot[laststep - i])
        
        #Feed in the last three x- and y-points into the intrpf function to
        #find the final x position at y = 0.0
        MaxRange = intrpf(0.0,LastThreeY, LastThreeX)
        
        break 

xground = np.array([0., xNoAir[laststep-1]])
yground = np.array([0., 0.])
 
#Using the lists I appended to get back all x,y components of velocity for with and without air resistance.
#I did not want to much going on inside of the step loop, as it is already hard to read as is.
#The vAir and vNoAir lists have x or y components of velocity based on index.  
vxAir = [v[0] for v in vAir]
vyAir = [v[1] for v in vAir]
vxNoAir = [v[0] for v in vNoAir]
vyNoAir = [v[1] for v in vNoAir]

speedAir = np.sqrt(vxAir[-1]**2 + vyAir[-1]**2) #Speed of the last velocity, magnitude of the x, y components. 
speedNoAir = np.sqrt(vxNoAir[-1]**2 + vyNoAir[-1]**2)

#The final speed, and (x,y) velocities printed out.
#For Question #1.
print('AIR RESISTANCE CASE')
print ('The final speed, and (x,y) components of velocity were: ')
print('Speed => ', speedAir)
print('x direction =>' , vxAir[-1] , ' m/s' )
print('y direction =>' , vyAir[-2] , ' m/s' )
print()
print('NO AIR RESISTANCE CASE')
print ('The final speed, and (x,y) components of velocity were: ')
print('Speed => ', speedNoAir)
print('x direction => ' , vxNoAir[-1] , ' m/s' )
print('y direction => ' , vyNoAir[-2] , ' m/s' )

#I wanted to be able to see the final stuff before spitting out the plot every time.
#For Question #2. 
seePlot = input('\nEnter 1 to display the velocity, and position plots >> ')

if seePlot == '1':
    showPlots(vxAir, vyAir, vxNoAir, vyNoAir, xground, yground)


