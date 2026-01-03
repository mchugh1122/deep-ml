# Cell 1
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Handle edge case of empty matrix
    if not a or not a[0]:
        return []
    
    # Using list comprehension to create the transposed matrix
    # For each column index j, create a new row from the j-th element of each original row
    return [[row[j] for row in a] for j in range(len(a[0]))]