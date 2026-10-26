import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.
    
    Args:
        gradient: A list representing the gradient vector
    
    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """
    grad_arr = np.array(gradient, dtype=float)
    magnitude = float(np.linalg.norm(grad_arr))
    
    # Handle the zero-vector edge case to prevent division by zero
    if magnitude == 0.0:
        zero_vec = np.zeros_like(grad_arr).tolist()
        return {
            "magnitude": 0.0,
            "direction": zero_vec,
            "descent_direction": zero_vec
        }
    
    # Unit vector pointing in steepest ascent direction
    direction = (grad_arr / magnitude).tolist()
    
    # Unit vector pointing in steepest descent direction
    descent_direction = (-grad_arr / magnitude).tolist()
    
    return {
        "magnitude": magnitude,
        "direction": direction,
        "descent_direction": descent_direction
    }