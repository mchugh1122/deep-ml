import numpy as np


def compute_norm(arr, norm_type):
    # Ensure input is a NumPy array
    arr = np.asarray(arr)

    # Validate norm_type and compute requested norm
    if norm_type == "l1":
        # Entrywise L1: Sum of absolute values
        return float(np.sum(np.abs(arr)))

    elif norm_type == "l2":
        # Entrywise L2: Square root of the sum of squared entries
        return float(np.sqrt(np.sum(np.square(arr))))

    elif norm_type == "linf":
        # Entrywise L-infinity: Maximum absolute value
        return float(np.max(np.abs(arr)))

    elif norm_type == "frobenius":
        # Frobenius norm requires a 2D matrix
        if arr.ndim != 2:
            raise ValueError(
                "Frobenius norm requires a 2D matrix (array with 2 dimensions)."
            )
        return float(np.sqrt(np.sum(np.square(arr))))

    else:
        raise ValueError(
            f"Unsupported norm_type '{norm_type}'. Expected 'l1', 'l2', 'linf', or 'frobenius'."
        )


# Example Usage:
arr = np.array([[1, 2], [3, 4]])

print(
    f"Frobenius Norm: {compute_norm(arr, 'frobenius'):.4f}"
)  # Output: 5.4772
print(f"L1 Norm: {compute_norm(arr, 'l1')}")  # Output: 10.0
print(f"L-inf Norm: {compute_norm(arr, 'linf')}")  # Output: 4.0