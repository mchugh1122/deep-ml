def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    n = len(matrix)
    
    # Edge case for empty matrix
    if n == 0:
        return 0.0, 0.0
        
    # 1. Compute Trace (Sum of main diagonal elements)
    trace = float(sum(matrix[i][i] for i in range(n)))
    
    # 2. Compute Determinant (Recursive cofactor expansion)
    def get_determinant(mat: list[list[float]]) -> float:
        size = len(mat)
        
        # Base case: 1x1 matrix
        if size == 1:
            return float(mat[0][0])
            
        # Base case: 2x2 matrix
        if size == 2:
            return float(mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0])
            
        det = 0.0
        for c in range(size):
            # Create (size-1) x (size-1) submatrix by excluding row 0 and column c
            submatrix = [
                [mat[r][col] for col in range(size) if col != c] 
                for r in range(1, size)
            ]
            
            # Alternate signs: + - + -
            sign = (-1) ** c 
            det += sign * mat[0][c] * get_determinant(submatrix)
            
        return det
        
    determinant = get_determinant(matrix)
    
    return determinant, trace