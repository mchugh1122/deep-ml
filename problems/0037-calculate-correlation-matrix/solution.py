import numpy as np

def calculate_correlation_matrix(X: np.ndarray, Y: np.ndarray = None) -> np.ndarray:
    """
    Calculate the Pearson correlation matrix for X (or between X and Y).
    
    Args:
        X: 2D numpy array of shape (n_samples, n_features_X)
        Y: Optional 2D numpy array of shape (n_samples, n_features_Y)
        
    Returns:
        Correlation matrix as a 2D numpy array.
    """
    X = np.asarray(X, dtype=float)
    
    if Y is None:
        # np.corrcoef treats rows as variables by default, so transpose X
        return np.corrcoef(X.T)
    
    Y = np.asarray(Y, dtype=float)
    
    # Center both matrices
    X_centered = X - np.mean(X, axis=0)
    Y_centered = Y - np.mean(Y, axis=0)
    
    # Standard deviation along columns (using population std, ddof=0)
    std_X = np.std(X, axis=0, ddof=0)
    std_Y = np.std(Y, axis=0, ddof=0)
    
    # Cross-covariance matrix normalized by n
    n_samples = X.shape[0]
    cov_XY = np.dot(X_centered.T, Y_centered) / n_samples
    
    # Compute denominator matrix
    outer_std = np.outer(std_X, std_Y)
    
    # Avoid division by zero
    outer_std[outer_std == 0] = 1.0
    
    return cov_XY / outer_std