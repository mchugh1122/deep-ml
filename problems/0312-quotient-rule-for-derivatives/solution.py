from typing import List

def eval_poly(coeffs: List[float], x: float) -> float:
    """Evaluates polynomial given descending power coefficients at point x."""
    val = 0.0
    degree = len(coeffs) - 1
    for i, c in enumerate(coeffs):
        power = degree - i
        val += c * (x ** power)
    return val

def eval_poly_derivative(coeffs: List[float], x: float) -> float:
    """Evaluates the derivative of a polynomial at point x using power rule."""
    val = 0.0
    degree = len(coeffs) - 1
    for i, c in enumerate(coeffs):
        power = degree - i
        if power > 0:
            val += c * power * (x ** (power - 1))
    return val

def quotient_rule_derivative(g_coeffs: List[float], h_coeffs: List[float], x: float) -> float:
    # 1. Compute function values at x
    g_val = eval_poly(g_coeffs, x)
    h_val = eval_poly(h_coeffs, x)
    
    # 2. Compute derivative values at x
    g_prime = eval_poly_derivative(g_coeffs, x)
    h_prime = eval_poly_derivative(h_coeffs, x)
    
    # 3. Apply the quotient rule: (g' * h - g * h') / (h^2)
    return (g_prime * h_val - g_val * h_prime) / (h_val ** 2)

# --- Verification matching the problem statement ---
g_coeffs = [1, 0, 1]
h_coeffs = [1, 2]
x = 2.0

result = quotient_rule_derivative(g_coeffs, h_coeffs, x)
print(f"Output: {result}")  # Output: 0.6875