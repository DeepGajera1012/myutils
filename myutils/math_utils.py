def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def substract(a: int, b: int) -> int:
    """Subtract two integers."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

def divide(a: int, b: int) -> float:
    """Divide two integers. Returns float."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base: int, exp: int) -> int:
    """Raise a number to a power."""
    return base ** exp