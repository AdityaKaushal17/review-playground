def add(a, b): return a + b
def divide(a, b):
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
def average(xs): return sum(xs) / len(xs) if xs else 0.0
def clamp(x, lo, hi): return max(lo, min(x, hi))
