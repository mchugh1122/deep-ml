import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    # Create a float copy of the matrix to avoid integer truncation 
    # and to preserve the original matrix
    mat = np.array(A, dtype=float, copy=True)
    m, n = mat.shape
    
    rank = 0
    row_idx = 0
    
    # Iterate through columns to find pivots
    for col_idx in range(n):
        # If we've processed all rows, we can't find more independent rows
        if row_idx >= m:
            break
            
        # Find the pivot element (maximum absolute value in the current column)
        # We only look at the current row and below
        pivot_offset = np.argmax(np.abs(mat[row_idx:m, col_idx]))
        pivot_r = row_idx + pivot_offset
        
        # If the pivot element is effectively zero, skip this column
        # as it is linearly dependent on previous columns
        if np.abs(mat[pivot_r, col_idx]) <= tol:
            continue
            
        # Swap the current row with the pivot row to maximize numerical stability
        if pivot_r != row_idx:
            mat[[row_idx, pivot_r]] = mat[[pivot_r, row_idx]]
            
        # Eliminate all entries below the current pivot
        for i in range(row_idx + 1, m):
            factor = mat[i, col_idx] / mat[row_idx, col_idx]
            # Subtract the scaled pivot row from the current row
            mat[i, col_idx:] -= factor * mat[row_idx, col_idx:]
            
        # We found a valid pivot, meaning we found a linearly independent dimension
        rank += 1
        row_idx += 1
        
    return rank