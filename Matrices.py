"""Problem 01
In this exercise, your main goal is to get familiar with the basic numpy operations. Complete the function play_with_matrices() by following these steps in order:

create a matrix m1 of size 4x2 by drawing samples from a standard Normal distribution (mean=0, stdev=1). Hint: use np.random.standard_normal function
create another matrix m2 of size 4x2 by drawing samples from a standard Normal distribution
Multiply the m1 with the maximum value of matrix m2
Square all elements of m2 using np.square
Multiply resulting matrix in 3. with the transpose of the resulting matrix in 4. using matrix multiplication
Compute and return the eigenvalues of the resulting matrix in (5). using linear algebra (imported as LA) """

import numpy as np
from numpy import linalg as LA

def play_with_matrices() -> np.ndarray:
    # Write Code Here
    m1 = np.random.standard_normal(size=(4,2))
    m2 = np.random.standard_normal(size=(4,2))
    max_m2 = m2.max()
    m3 = max_m2 * m1
    m4 = np.square(m2) 
    m5 = np.dot(m3,m4.transpose())
    w,v = LA.eig(m5)
    return (w,v)

play_with_matrices()
