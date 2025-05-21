#brute force
def bpower(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

# divide and conquer
def dpower(a, n):
    if n == 0:
        return 1
    half = dpower(a, n // 2)
    return half * half if n % 2 == 0 else a * half * half

a = int(input("Enter base: "))
n = int(input("Enter exponent: "))
print("Brute Force:", bpower(a, n))
print("Divide & Conquer:", dpower(a, n))
