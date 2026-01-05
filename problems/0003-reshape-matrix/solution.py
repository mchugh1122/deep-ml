# Cell 1
import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    try:
        # Convert input to numpy array
        np_array = np.array(a)
        
        # Try to reshape - will raise ValueError if shapes are incompatible
        reshaped = np_array.reshape(new_shape)
        
        # Convert back to nested list using tolist()
        return reshaped.tolist()
    
    except (ValueError, AttributeError):
        # Return empty list if reshaping fails
        return []