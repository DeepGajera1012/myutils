def _validate_numeric(name: str, value) -> None:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"Parameter '{name}' must be an instance of int or float, not {type(value).__name__}")

def _validate_integer(name: str, value) -> None:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"Parameter '{name}' must be an instance of int, not {type(value).__name__}")

def add(a: int, b: int) -> int:
    """Add two integers."""
    _validate_numeric('a', a)
    _validate_numeric('b', b)
    return a + b

def substract(a: int, b: int) -> int:
    """Subtract two integers."""
    _validate_numeric('a', a)
    _validate_numeric('b', b)
    return a - b

def subtract(a: int, b: int) -> int:
    """Subtract two integers."""
    return substract(a, b)

def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    _validate_numeric('a', a)
    _validate_numeric('b', b)
    return a * b

def divide(a: int, b: int) -> float:
    """Divide two integers. Returns float."""
    _validate_numeric('a', a)
    _validate_numeric('b', b)
    if b == 0 or b == 0.0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base: int, exp: int) -> int:
    """Raise a number to a power."""
    _validate_integer('base', base)
    _validate_integer('exp', exp)
    if exp < 0:
        raise ValueError("Negative exponent is not supported for integer power")
    if exp > 10000:
        raise ValueError("Exponent exceeds maximum safe limit of 10000 to prevent Denial of Service")
    return base ** exp