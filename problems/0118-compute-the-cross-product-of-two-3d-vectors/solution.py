import numpy as np

def cross_product(a: list, b: list) -> list:
    """
    Computes the cross product of two 3-dimensional vectors using NumPy.
    """
    return np.cross(a, b).tolist()

# Verification matching the example in image_17849e.png:
result = cross_product([1, 0, 0], [0, 1, 0])
print(result)  # Output: [0, 0, 1]