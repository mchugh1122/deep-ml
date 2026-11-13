import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix.
    
    Args:
        A: 2x2 numpy array
    
    Returns:
        U: 2x2 orthogonal matrix (left singular vectors)
        s: 1D array of singular values
        V: 2x2 matrix (right singular vectors)
    """
    A = np.array(A, dtype=float)
    ATA = A.T @ A
    
    E = ATA[0, 0]
    F = ATA[0, 1]
    G = ATA[1, 1]
    
    # Compute eigenvalues of A^T A (trace and determinant via gap)
    trace = E + G
    diff = E - G
    gap = np.sqrt(diff**2 + 4 * F**2)
    
    l1 = (trace + gap) / 2
    l2 = (trace - gap) / 2
    
    # Singular values are the square roots of the eigenvalues
    s1 = np.sqrt(max(0.0, l1))
    s2 = np.sqrt(max(0.0, l2))
    
    # Compute right singular vectors (eigenvectors of A^T A)
    if gap < 1e-14:
        v1 = np.array([1.0, 0.0])
        v2 = np.array([0.0, 1.0])
    else:
        # Evaluate both analytical eigenvectors to avoid numerical zero-vector issues
        vec_a = np.array([F, l1 - E])
        vec_b = np.array([l1 - G, F])
        
        # Pick the most stable (largest norm) vector before normalizing
        if np.linalg.norm(vec_a) >= np.linalg.norm(vec_b):
            v1 = vec_a / np.linalg.norm(vec_a)
        else:
            v1 = vec_b / np.linalg.norm(vec_b)
            
        # The second eigenvector is orthogonal to the first in 2D space
        v2 = np.array([-v1[1], v1[0]])
        
    # Compute left singular vectors (U) using the relation A v_i = s_i u_i
    if s1 > 1e-12:
        u1_raw = A @ v1
        u1 = u1_raw / np.linalg.norm(u1_raw)
    else:
        u1 = np.array([1.0, 0.0])
        
    if s2 > 1e-12:
        u2_raw = A @ v2
        # Use Gram-Schmidt against u1 to ensure exact numerical orthogonality
        if np.linalg.norm(u2_raw) > 1e-12:
            u2 = u2_raw - np.dot(u2_raw, u1) * u1
            u2 = u2 / np.linalg.norm(u2)
        else:
            u2 = np.array([-u1[1], u1[0]])
    else:
        # If s2 is effectively zero, just take the orthogonal complement of u1
        u2 = np.array([-u1[1], u1[0]])
        
    U = np.column_stack((u1, u2))
    s = np.array([s1, s2])
    V = np.array([v1, v2])
    
    return U, s, V