"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):

    for x in range(len(matrix)):
        ret_str = ""
        for y in range(len(matrix)):
            ret_str += str(matrix[x][y]) + "\t"
        print (ret_str)
    pass

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if (x == y):
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0
    pass

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for row in range(len(m2)):
        temp_col = []
        for col in range(len(m1)):
            temp_col.append(m2[row][col])
        for col in range(len(m1)):
            sum = 0
            for k in range(len(m1)):
                sum += temp_col[k] * m1[k][col]
            m2[row][col] = sum
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
'''
m1 = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]]
m2 = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]]
m5 = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,1,1,1]]


m3 = [[1,2], [3, 4]]
m4 = [[1,0], [0, 1]]
print_matrix(m1)
#ident(m2)
print_matrix(m2)
matrix_mult(m1, m2)
print_matrix(m2)
'''
