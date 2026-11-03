import numpy as np

def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.

    :param v: The vector to be projected
    :param L: The line vector defining the direction of projection
    :return: List representing the projection of v onto L
    """
    v_arr = np.array(v, dtype=float)
    L_arr = np.array(L, dtype=float)
    
    # Compute dot products: (v · L) and (L · L) = ||L||^2
    dot_v_L = np.dot(v_arr, L_arr)
    dot_L_L = np.dot(L_arr, L_arr)
    
    # Handle zero vector case for L
    if dot_L_L == 0:
        return [0.0] * len(v)
        
    # proj_L(v) = ((v · L) / ||L||^2) * L
    projection = (dot_v_L / dot_L_L) * L_arr
    
    # Return rounded values to 3 decimal places
    return [round(float(x), 3) for x in projection]