from typing import Tuple

def cbc_envelope(x: Tuple[float, float], bounds: Tuple[Tuple[float,float], Tuple[float,float]]) -> bool:
    """Simple 2D box constraint as a CBC stand-in. True if safe."""
    (xmin, xmax), (ymin, ymax) = bounds
    return (xmin <= x[0] <= xmax) and (ymin <= x[1] <= ymax)