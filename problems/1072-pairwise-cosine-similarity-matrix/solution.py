import numpy as np

def pairwise_cosine_similarity(X):
    X = np.array(X, dtype=float)
    
    # Compute L2 norms along axis 1 (rows)
    norms = np.linalg.norm(X, axis=1)
    
    # Compute matrix multiplication X @ X^T for dot products
    dot_products = X @ X.T
    
    # Outer product of norms gives matrix of denominator terms: ||x_i|| * ||x_j||
    norm_matrix = np.outer(norms, norms)
    
    # Mask where both rows have non-zero norms
    valid_mask = norm_matrix > 0.0
    
    # Compute pairwise cosine similarity safely
    S = np.zeros_like(dot_products)
    S[valid_mask] = dot_products[valid_mask] / norm_matrix[valid_mask]
    
    # Round to 4 decimal places and convert to nested list
    return np.round(S, 4).tolist()