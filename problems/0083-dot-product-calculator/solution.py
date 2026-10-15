import numpy as np

def calculate_dot_product(vec1, vec2):
    # 1. Safety: Guard clause catches length mismatches
    if len(vec1) != len(vec2):
        return -1

    # 2 & 3. Readability & Memory Efficiency: Generator expression with zip
    return sum(x * y for x, y in zip(vec1, vec2))

