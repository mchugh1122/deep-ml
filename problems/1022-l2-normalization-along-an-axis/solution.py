import numpy as np

def l2_normalize(x: np.ndarray, axis: int = -1, eps: float = 1e-12) -> list:
    """
    L2-normalize x along the given axis.

    Args:
        x: input NumPy array
        axis: axis along which to normalize
        eps: small constant for numerical stability

    Returns:
        Normalized array as a nested Python list.
    """
    # Sum of squares along the specified axis, keeping dimensions for broadcasting
    sum_sq = np.sum(np.square(x), axis=axis, keepdims=True)
    
    # Compute the norm with the epsilon term inside the square root
    norm = np.sqrt(sum_sq + eps)
    
    # Perform element-wise division and convert to a nested Python list
    normalized = x / norm
    return normalized.tolist()