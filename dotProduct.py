import numpy as np

#N-dimensional dot product, code is straight forward enough to read. 

vectorU = []
dimension = 1
while True:
    u = input('Enter vector u\'s component #' + str(dimension) + ', or enter \'Next\' to enter the next vector.\n')
    if u.lower() == 'next':
        print()
        break
    dimension += 1
    vectorU.append(int(u))

vectorV = []
dimension = 1
while True:
    v = input('Enter vector v\'s component #' + str(dimension) + ', or enter \'Calculate\' to calculate their dot product.\n')
    if v.lower() == 'calculate':
        print()
        break
    dimension += 1
    vectorV.append(int(v))

print()    

print('Vector u: ' + str(vectorU))
print('Vector v: ' + str(vectorV))

npU = np.array(vectorU)
npV = np.array(vectorV)

if len(npU) != len(npV):
    print('Vectors must have the same number of dimensions to calculate their dot product.')

else:
    dotProduct = 0
    for i in range(len(npU)):
        dotProduct = npU[i] * npV[i] + dotProduct

    if dotProduct == 0:
        print('These vectors are orthogonal, their dot product is 0.')
    else:
        print('These vectors are not orthogonal, their dot product is ' + str(dotProduct) + '.')
        

