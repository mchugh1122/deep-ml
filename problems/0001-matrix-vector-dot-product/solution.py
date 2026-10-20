import numpy as np


def matrix_dot_vector(a, b):
    
    a_arr = np.array(a)
    b_arr = np.array(b)

    if a_arr.ndim != 2 or a_arr.shape[1] != len(b_arr):
        return -1

    return (a_arr @ b_arr).tolist()



