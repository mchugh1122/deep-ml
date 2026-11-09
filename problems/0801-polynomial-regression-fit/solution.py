import numpy as np

def fit_polynomial(x, y, degree):
    """
    Fit a polynomial of the given degree to (x, y) by least squares.

    Args:
        x: list/array of input values, length n
        y: list/array of target values, length n
        degree: non-negative integer, the polynomial degree

    Returns:
        List of coefficients [c_0, c_1, ..., c_degree] in increasing power order.
    """
    x_arr = np.array(x, dtype=float)
    y_arr = np.array(y, dtype=float)

    # Build the Vandermonde matrix with powers from 0 to degree: [x^0, x^1, ..., x^d]
    X_mat = np.vander(x_arr, degree + 1, increasing=True)

    # Solve the ordinary least-squares problem X_mat * c = y
    coeffs, _, _, _ = np.linalg.lstsq(X_mat, y_arr, rcond=None)

    return coeffs.tolist()