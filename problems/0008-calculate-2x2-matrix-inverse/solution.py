# Cell 1
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    # Validate input shape: 2x2 matrix
    if not isinstance(matrix, list) or len(matrix) != 2:
        return None
    if not all(isinstance(row, list) and len(row) == 2 for row in matrix):
        return None

    a, b = matrix[0]
    c, d = matrix[1]

    try:
        det = a * d - b * c
    except Exception:
        return None

    # If determinant is zero, matrix is singular
    if det == 0:
        return None

    inv_det = 1 / det

    # Return on a single line to avoid parser errors in the environment
    return [[d * inv_det, -b * inv_det], [-c * inv_det, a * inv_det]]