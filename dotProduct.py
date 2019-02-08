import numpy as np

#N-dimensional dot product, code is straight forward enough to read. 

vectorU = []
while True:
    u = input('Enter vector u\'s component, or enter \'v\' to enter the next vector.\n')
    if u.lower() == 'v':
        print()
        break
    vectorU.append(int(u))

vectorV = []
while True:
    v = input('Enter vector v\'s components, or enter \'Calculate\' to calculate the dot product.\n')
    if v.lower() == 'calculate':
        print()
        break
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
        

