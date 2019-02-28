import numpy as np
import matplotlib.pyplot as plt

#Interpolation - the insertion of an intermediate value or term into a series by estimating or calculating it from surrounding known values.
#(Google dictionary)
#Basically a mathematical estimate based on data. 

def interpolate(xi, xyPairs): #Takes a list of ordered pairs  
    x = [xy[0] for xy in xyPairs] #Lists of x and y values 
    y = [xy[1] for xy in xyPairs]
    
    yi = ( (xi-x[1])*(xi-x[2])/((x[0]-x[1])*(x[0]-x[2])) * y[0]
    + (xi-x[0])*(xi-x[2])/((x[1]-x[0])*(x[1]-x[2])) * y[1]
    + (xi-x[0])*(xi-x[1])/((x[2]-x[0])*(x[2]-x[1])) * y[2] )

    return yi

def main():
    print('You will enter three (x, y) pairs to interpolate data using Lagrange polynomials.')
    xyPairs = []
    for i in range(3):
        xComponent = input('Enter the value of x >> ')
        yComponent = input('Enter the corresponding value of y >> ')
        xyPairs.append((int(xComponent), int(yComponent)))

    xyPairs = np.array(xyPairs)
    xi = int(input('Enter an x value to interpolate at  >> ')) #Uses this x to calculate yi based on the  
                                                               #Entered ordered pairs

    #Checked with >> x^2 - 6x + 9, Ordered pairs: [(5,4), (2,1), (4,1)], xi = 10.
    #Returns 49.0, which is correct (10)^2 - 6(10) + 9 = 49
    print('Interpolation based on data input => ' + str(interpolate(xi, xyPairs)))
    print()

    xMin = int(input('Enter the lowest x value you want to interpolate from >> '))#Range of x values 
    xMax = int(input('Enter the max x value you want to interpolate to >> '))     #Graphs x and interpolated y in range 
    xr = np.array([xMin,xMax])

    nplot = 100 
    xi = np.empty(nplot)
    yi = np.empty(nplot)

    for i in range(nplot) :
        xi[i] = xr[0] + (xr[1]-xr[0])* i/float(nplot)
        yi[i] = interpolate(xi[i], xyPairs)

    x = [xy[0] for xy in xyPairs]
    y = [xy[1] for xy in xyPairs]
        
    plt.plot(x, y, '*', xi, yi , '-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Three point interpolation')
    plt.legend(['Data points','Interpolation  '])
    plt.show()

main()
