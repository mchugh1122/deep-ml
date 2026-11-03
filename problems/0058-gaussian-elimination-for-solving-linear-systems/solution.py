import numpy as np

def gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
    :param A: Coefficient matrix
    :param b: Right-hand side vector
    :return: Solution vector x
    """
    # Create float copies to avoid modifying original inputs or precision loss
    A = np.array(A, dtype=float, copy=True)
    b = np.array(b, dtype=float, copy=True)
    n = len(b)
    
    # Step 1: Forward Elimination with Partial Pivoting
    for i in range(n):
        # Locate maximum element in column i from row i down
        pivot_idx = i + np.argmax(np.abs(A[i:, i]))
        
        # Swap current row with pivot row in both A and b
        if pivot_idx != i:
            A[[i, pivot_idx]] = A[[pivot_idx, i]]
            b[[i, pivot_idx]] = b[[pivot_idx, i]]
            
        # Eliminate entries below the diagonal pivot
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
            
    # Step 2: Backward Substitution
    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
        
    return x