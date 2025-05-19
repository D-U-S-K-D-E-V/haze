def clamp(x: float, min_val: float = 0.1, max_val: float = 0.9) -> float:
    return max(min(x, max_val), min_val)