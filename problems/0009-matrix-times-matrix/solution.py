import numpy as np


def matrixmul(a, b):
    a_arr = np.array(a)
    b_arr = np.array(b)

    # Check if both are 2D matrices and if columns of A match rows of B
    if (
        a_arr.ndim != 2
        or b_arr.ndim != 2
        or a_arr.shape[1] != b_arr.shape[0]
    ):
        return -1

    return (a_arr @ b_arr).tolist()