from pprint import pprint
import numpy as np

print('Homework 4 check.')
print()

coefficientsA = np.array([[1, 1, 1], [3, 1, 0], [-1, 0, 1]])
rhs = np.array([[6], [11], [-2]])
print('Chapter 4 excercise 5(a)')
print(np.linalg.solve(coefficientsA, rhs))

print()

coefficientsB = np.array([[1, 1, 1], [-1, 0, 1], [3, 1, 0]])
rhs = np.array([[6], [-2], [11]])
print('Chapter 4 excercise 5(b)')
print(np.linalg.solve(coefficientsB, rhs))

#I attempted option B it was harder than I thought. 
'''
matrix = [[1,1,1,6], [3,1,0,11], [-1,0,1,-2]]
for i, row in enumerate(matrix):

    diffRows = ([row for row in matrix if matrix[i] != row]) #The other rows, does not the row current element. 

    for diffRow in diffRows:

        if diffRow[i] + row[i] == 0: #If within a different row, the two elements added = 0,
                                     #Add the other row to orginal matrix being looped in the main for, changing 'row'
            for j in range(len(row)):
                row[j] = row[j] + diffRow[j]
                
            break #Only want to see one change to a row at a time. 


    print(row)
    print()
'''      
                

            
