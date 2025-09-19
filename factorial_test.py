import time
import sys

# Fix for large integer string conversion
sys.set_int_max_str_digits(50000)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def time_factorial(func, n, name):
    start = time.time()
    try:
        result = func(n)
        end = time.time()
        digits = len(str(result))
        print(f"{name} factorial({n}): {end - start:.6f}s, {digits} digits")
        return True
    except RecursionError:
        print(f"{name} factorial({n}): RecursionError")
        return False

if __name__ == "__main__":
    # Increase recursion limit for Python
    sys.setrecursionlimit(15000)
    
    test_values = [100, 1000, 5000, 10000]
    
    for n in test_values:
        print(f"\nTesting n = {n}")
        time_factorial(factorial_iterative, n, "Iterative")
        time_factorial(factorial_recursive, n, "Recursive")

