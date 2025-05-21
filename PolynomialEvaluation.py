import time

def poly_bf(coeffs, x):
    result = 0
    n = len(coeffs)
    for i in range(n):
        term = coeffs[i]
        for _ in range(n - i - 1):
            term *= x
        result += term
    return result

def horner(coeffs, x):
    result = coeffs[0]
    for i in range(1, len(coeffs)):
        result = result * x + coeffs[i]
    return result

poly = [2, -6, 2, -1]  # 2x^3 - 6x^2 + 2x - 1
x = 3
print("Brute Force:", poly_bf(poly, x))
print("Horner’s:", horner(poly, x))
