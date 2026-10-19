import numpy as np


def cosine_similarity(v1, v2):
    # Step 1: Calculate the dot product (numerator)
    dot_product = np.dot(v1, v2)

    # Step 2: Calculate L2 norms / lengths of both vectors (denominator)
    length_v1 = np.linalg.norm(v1)
    length_v2 = np.linalg.norm(v2)

    # Step 3: Divide dot product by product of lengths
    return dot_product / (length_v1 * length_v2)
