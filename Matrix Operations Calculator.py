# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:42:02 2024

@author: rravu
"""

from math import e
from math import pi

class matrix():
    
    def __init__(self, matrix):
        self.matrix = matrix
        
    def __add__(self, matrix2):
        
        Result = []
        while len(Result) != len(self.matrix):
            Result.append([])
        for i in range(len(Result)):
            Result[i] = [0 for num in self.matrix[0]]
        
        for row in range(len(self.matrix)):
            for element in range(len(self.matrix[0])):
                Result[row][element] = self.matrix[row][element] + matrix2.matrix[row][element] 
                
        return Result
                
    def __sub__(self, matrix2):
        Result = []
        while len(Result) != len(self.matrix):
            Result.append([])
        for i in range(len(Result)):
            Result[i] = [0 for num in self.matrix[0]]
        
        for row in range(len(self.matrix)):
            for element in range(len(self.matrix[0])):
                Result[row][element] = self.matrix[row][element] - matrix2.matrix[row][element] 
                
        return Result
        
    def __mul__(self, matrix2):
        t2 = matrix2.transpose() # NOTE: in the real world, you can NOT multiply two given matrices by taking the transpose of the second matrix.
                                 # I am simply doing so because it is easier to multiply row x column by imposing a transpose function.
        Result = []
        # The dimensions of the product matrix of two matrices is the # rows of the first matrix X the # of columns of the second matrix
        while len(Result) != len(self.matrix): # initializing Result matrix as having the same # of rows as matrix1
            Result.append([])
        
        while len(Result[0]) != len(matrix2.matrix[0]): # initializing Result matrix as having the same # of columns as matrix2
            for i in range(len(Result)):
                Result[i] = [0 for num in matrix2.matrix[0]]   
        
        for i in range(len(Result)):
            for j in range(len(Result[0])):
                Result[i][j] = matrix2.sum_list(self.matrix[i], t2[j])
        
        return Result
    
    def Scalar_multiply(self, scalar):
        Result = []
        for row in self.matrix:
            Result.append([num*scalar for num in row])
        return Result
    
    def transpose(self):
        transpose = []
        while len(transpose) != len(self.matrix):
            transpose.append([])
        for row in self.matrix:
            for i in range(len(self.matrix[0])):
                transpose[i].append(row[i])
        return transpose
    
    def sum_list(self, list1, list2):
        sumy = []
        for i in range(len(list1)):
            sumy.append(list1[i]*list2[i])
        return round(sum(sumy), 1)  
    
    
        
def create():
    
    rows = input('\nplease specify the number of rows of your matrix: '.upper())
    
    while rows.strip().isnumeric() == False:
        print('\nYou did not provide a valid numeric input for the # of rows')
        rows = input('\nplease specify the number of rows of your matrix: '.upper())
    
    rows = eval(rows.replace('^', '**'))
    
    matrix = []

    while len(matrix) != rows:
        matrix.append([])
      
    for i in range(len(matrix)):
        user = input(f'\nPlease enter the entries of row {i+1} of your matrix (with spaces): '.upper())
        row = user.split(' ') # Split() creates a list of items based on a specified seperator
        while "" in row: 
            row.remove('') # remove() only removes the first occurance of a specified item. We must use a while loop to remove
                           # all occurances
        while ' ' in row:
            row.remove(' ')
        matrix[i] = [eval(num) for num in row]
    
    return matrix

def operations():
    print('Welcome to my matrix calculator! Here are the available operations you can perform:'.upper())
    print('\nadd/substract: In order to add or subtract two matrices, you must ensure they are of the same dimension. i.e 4 x 3 and 4 x 3')
    print('\nscalar multiplication: scalar multiplicaton involves taking a constant, c, and multiplying that constant for every entry of a matrix to get an end result')
    print('\nmatrix multiplication: matrix multiplication involves taking two matrices, and multiplying the rows of the first matrix with the columns of the second matrix')
    print('\nin order to multiply two matrices, you must ensure that the number of rows of the first matrix is equivalent to the number of columns of the second matrix. ', end='')
    print('You can NOT multiply two matrices where the number of rows of the first matrix are not equal to the number of columns of the second matrix')
    
    print('\nWith that being said, lets analyze your FIRST matrix')
    
    matrix1 = create()
    print('\nBased on your inputs, is this your matrix?')
    for i in range(len(matrix1)): print(matrix1[i])
    validity = input('\n(a) yes \n(b) no \nanswer: ')
    
    while validity == 'b':
        print('Please re-enter your matrix')
        matrix1 = create()
        print('\nBased on your inputs, is this your matrix?')
        for i in range(len(matrix1)): print(matrix1[i])
        validity = input('\n(a) yes \n(b) no \nanswer: ')
        
    
    matrix1Dim = f'{len(matrix1)} x {len(matrix1[0])}'
    
    print('\nPlease describe which operations you want to perform on your matrix:')
    operation = input('(a) scalar multiplication \n(b) matrix multiplication \n(c) matrix addition \n(d) matrix subtraction \nanswer: ').lower().replace(' ', '')
    
    addOrsub = ['c', 'd']
    if operation in addOrsub:
        print('\nIn order to add or subtract two given matrices, they must be of exact same dimension')
        print('(i.e a 4 x 3 matrix being subtracted from a 4 x 3 matrix)')
        print('\nPlease make sure that the second matrix you will enter is of the same dimension as the first matrix')
        print('\nNow, let us analyze your SECOND matrix')
        matrix2 = create()
        matrix2Dim = f'{len(matrix2)} x {len(matrix2[0])}'
        matrix1 = matrix(matrix1)
        matrix2 = matrix(matrix2)
        if matrix1Dim != matrix2Dim:
           print('\nYour matrices have different dimensions. This operation is not possible'.upper())
           Result = None
           
        elif operation == 'c':
            Result = matrix1 + matrix2
            print('\nANSWER:')
            for row in Result: print(row)
            
        else:
            Result = matrix1 - matrix2
            print('\nANSWER: ')
            for row in Result: print(row)
            
    if operation == 'b':
        print('\nIn order to multiply two given matrices, the number of COLUMNS of the FIRST matrix MUST be equal to ', end='')
        print('The number of ROWS of the SECOND matrix')
        print('\nexample: you can multiply a 3 x 4 matrix with a 4 x 2 matrix, but you can NOT multiply a 4 x 2 matrix with a 3 x 4 matrix')
        print('\nNow, let us analyze your SECOND matrix')
        matrix2 = create()
        if len(matrix1[0]) != len(matrix2):
            print(f'\nYour first matrix has {len(matrix1[0])} columns. Your second matrix has {len(matrix2)} rows'.upper())
            print('Therefore, this operation is NOT possible'.upper())
            Result = None
        else:
            matrix1 = matrix(matrix1)
            matrix2 = matrix(matrix2)
            Result = matrix1 * matrix2
            print('\nANSWER: ')
            for row in Result: print(row)
            
    if operation == 'a':
        matrix1 = matrix(matrix1)
        scalar = eval(input('\nPlease specify your scalar: ').replace(' ', '').replace('^','**'))
        Result = matrix1.Scalar_multiply(scalar)
        print('\nANSWER: ')
        for row in Result: print(row)
    
    return Result
    
def main():
    operations()
    
main()
    