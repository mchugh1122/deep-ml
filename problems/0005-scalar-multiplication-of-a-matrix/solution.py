def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    scaled_matrix = []
    
    # Outer Loop: Traverses the vertical axis (Rows)
    for r in range(num_rows):
        row_accumulator = []
        
        # Inner Loop: Traverses the horizontal axis (Columns)
        for c in range(num_cols):
            # Pointwise lookup, execution, and accumulation
            scaled_value = matrix[r][c] * scalar
            row_accumulator.append(scaled_value)
            
        scaled_matrix.append(row_accumulator)
        
    return scaled_matrix
pass