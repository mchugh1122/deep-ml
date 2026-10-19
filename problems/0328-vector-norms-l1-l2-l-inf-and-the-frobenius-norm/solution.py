import numpy as np


def compute_norm(arr, norm_type):
    if norm_type == "l1":
        return float(np.sum(np.abs(arr)))
    elif norm_type == "l2":
        return float(np.sqrt(np.sum(np.square(arr))))

    elif norm_type == "linf":
        return float(np.max(np.abs(arr)))

    elif norm_type == "frobenius":
        if arr.ndim != 2:
            raise ValueError(
                "Frobenius norm requires a 2D matrix (array with 2 dimensions)."
            )
        return float(np.sqrt(np.sum(np.square(arr))))

    else:
        raise ValueError(
            f"Unsupported norm_type '{norm_type}'. Expected 'l1', 'l2', 'linf', or 'frobenius'."
        )

