import numpy as np
#use dtype = 'int64'
def Gauss_lattice_reduction(v1, v2):
    while(True):
        if np.linalg.norm(v2) < np.linalg.norm(v1):
            v2, v1 = v1, v2
        m = np.dot(v1, v2) // np.dot(v1, v1)
        if m == 0:
            return v1, v2
        v2 = v2 - m * v1