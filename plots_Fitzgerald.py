import numpy as np
import matplotlib.pyplot as plt

#Interpolation - the insertion of an intermediate value or term into a series by estimating or calculating it from surrounding known values.
#(Google dictionary)
#Basically a mathematical estimate based on data. 

def interpolate(xi, xComponents, yComponents):
    x = xComponents
    y = yComponents
    
    yi = ( (xi-x[1])*(xi-x[2])/((x[0]-x[1])*(x[0]-x[2])) * y[0]
    + (xi-x[0])*(xi-x[2])/((x[1]-x[0])*(x[1]-x[2])) * y[1]
    + (xi-x[0])*(xi-x[1])/((x[2]-x[0])*(x[2]-x[1])) * y[2] )

    return yi

print('You will type in (x, y) pairs to interpolate data using Lagrange polynomials.')
xyPairs = []
for i in range(3):
    xComponent = input('Enter the value of x >> ')
    yComponent = input('Enter the corresponding value of y >> ')
    xyPairs.append((int(xComponent), int(yComponent)))

xyPairs = np.array(xyPairs)
xComponents = xyPairs[:,0]
yComponents = xyPairs[:,1]

xi = int(input('Enter an x value to interpolate at  >> '))
   
#Checked with >> x^2 - 6x + 9, Ordered pairs: [(1,4), (2,1), (4,1)], xi = 5.
#Returns 4.0, which is correct (5)^2 - 6(5) + 9 = 4
userInterpolate = interpolate(xi, xComponents, yComponents)
print('Interpolation based on data input => ' + str(userInterpolate))
print()


#Range of x values. 
xMin = int(input('Enter the lowest x value you want to interpolate from >> '))
xMax = int(input('Enter the max x value you want to interpolate to >> '))
xr = np.array([xMin,xMax])

nplot = 100
xi = np.empty(nplot)
yi = np.empty(nplot)
           
for i in range(nplot) :
    xi[i] = xr[0] + (xr[1]-xr[0])* i/float(nplot)
    yi[i] = interpolate(xi[i], xComponents, yComponents)

plt.plot(xComponents, yComponents, '*', xi, yi , '-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Three point interpolation')
plt.legend(['Data points','Interpolation  '])
plt.show()






#I spent a long time trying to write the program as to generalize the series so you could enter many data points.
#But it would never give me the right answer.
#Used - https://www.dcode.fr/lagrange-interpolating-polynomial - to get how the series is defined.
#My old code that I thought was genius but didn't work.
#Probably completely pointless, as the 3 term series works just fine. 

"""
    numeratorTerms = []
    denominatorTerms = []
    seriesProduct = 1
    seriesSum = 0

    #Copies list, removes current x because the series has two iterators, but they can never be equal.
    #Append x back at the end so that it is not lost for the other x values. 
    for i, x in enumerate(xComponents):
        removeCurrentx = xComponents[:]
        print(len(removeCurrentx))
        removeCurrentx.remove(x)
        
        for otherx in removeCurrentx:
            numerator= xi - otherx     
            denominator = x - otherx
            seriesProduct = seriesProduct * (numerator / denominator)

        removeCurrentx.append(x)
        print(len(removeCurrentx))
        

        seriesProduct = seriesProduct * yComponents[i]
        seriesSum = seriesProduct + seriesSum
        
        
        
    #print(seriesSum)
"""
