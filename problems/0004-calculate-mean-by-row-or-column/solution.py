import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    # Step 1: Upgrade the plain Python list to a NumPy array
    np_matrix = np.array(matrix)
    
    # Step 2: Compute the mean along the requested dimensional axis
    if mode == 'row':
        # Calculate horizontally across columns (axis=1) -> yields a mean for each row
        means = np_matrix.mean(axis=1)
        
    elif mode == 'column':
        # Calculate vertically down rows (axis=0) -> yields a mean for each column
        means = np_matrix.mean(axis=0)
        
    else:
        # Safety gate: handle invalid mode inputs cleanly
        return []
        
    # Step 3 & 4: Convert back to a standard Python list and return
    return means.tolist()