# Cell 1
from typing import List, Union

def matrix_dot_vector(a: List[List[Union[int, float]]], b: List[Union[int, float]]) -> Union[List[Union[int, float]], int]:
    """
    Compute the dot product of a matrix and a vector.
    
    Args:
        a: Matrix represented as a list of lists (rows) of integers or floats
        b: Vector represented as a list of integers or floats
        
    Returns:
        Resulting vector as a list if dimensions are compatible, otherwise -1
    """
    # Check if matrix is empty
    if not a or not a[0]:
        return -1
    
    # Get dimensions
    rows = len(a)
    cols = len(a[0])
    
    # Check if all rows have the same number of columns
    for row in a:
        if len(row) != cols:
            return -1
    
    # Check dimension compatibility
    if cols != len(b):
        return -1
    
    # Compute the dot product
    result = []
    for i in range(rows):
        row_sum = 0
        for j in range(cols):
            row_sum += a[i][j] 