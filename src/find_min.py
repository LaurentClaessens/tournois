"""Find local minimum."""

from typing import Callable

from src.utilities import dprint


def find_min(fun: Callable[[list[float]], float], x0: list[float]):
    """Find local min from x0."""
    y0 = fun(x0)

    n = len(x0)
    for i in range(0, len(0, n)):
        dprint(f"on va faire la dérivée pour {i}")
