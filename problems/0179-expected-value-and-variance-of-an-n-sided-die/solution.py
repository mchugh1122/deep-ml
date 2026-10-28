def dice_statistics(n: int) -> tuple[float, float]:
    """
    Computes the expected value and variance of a fair n-sided die roll.
    
    Args:
        n: Number of sides on the die (numbered 1 through n)
        
    Returns:
        Tuple containing (expected_value, variance) rounded to 4 decimal places
    """
    expected_value = (n + 1) / 2.0
    variance = (n**2 - 1) / 12.0
    
    return round(expected_value, 4), round(variance, 4)

# --- Example Verification ---
exp_val, var = dice_statistics(6)
print(f"Expected Value: {exp_val}, Variance: {var}")
# Output: Expected Value: 3.5, Variance: 2.9167