import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    arr = np.asarray(data)
    
    # Calculate mode using np.unique
    vals, counts = np.unique(arr, return_counts=True)
    mode_val = float(vals[np.argmax(counts)])
    
    # Calculate summary metrics
    mean_val = float(np.mean(arr))
    median_val = float(np.median(arr))
    var_val = float(np.var(arr))  # Default ddof=0 divides by N
    std_val = float(np.std(arr))  # Default ddof=0 divides by N
    
    # Calculate percentiles and IQR
    p25 = float(np.percentile(arr, 25))
    p50 = float(np.percentile(arr, 50))
    p75 = float(np.percentile(arr, 75))
    iqr_val = p75 - p25
    
    return {
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val,
        "variance": var_val,
        "standard_deviation": std_val,
        "25th_percentile": p25,
        "50th_percentile": p50,
        "75th_percentile": p75,
        "interquartile_range": iqr_val,
    }