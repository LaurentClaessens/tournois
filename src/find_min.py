"""Find local minimum."""

from typing import Callable

from src.utilities import dprint
from src.utilities import ciao


epsilon = 0.00001
step = 0.1

Fun = Callable[['Point'], float]


class Vector:
    def __init__(self, v: list[float]):
        self.v = v

    def __getitem__(self, i):
        return self.v[i]

    def __mul__(self, l: float):
        """Return `self` multiplied by the scalar `l`."""
        new_v = [l*x for x in self.v]
        return Vector(new_v)

    def __neg__(self):
        return self * (-1)

    def __str__(self):
        s_x = [str(c) for c in self.v]
        return ",".join(s_x)


class Point:
    def __init__(self, x: list[float]):
        self.n = len(x)
        self.x = x

    def __getitem__(self, i: int):
        return self.x[i]

    def __add__(self, v: Vector) -> 'Point':
        new_list = []
        for i in range(0, self.n):
            new_list.append(self.x[i]+v[i])
        return Point(new_list)

    def __sub__(self, v: Vector) -> 'Point':
        return self + (-v)

    def __len__(self):
        return self.n

    def __str__(self):
        s_x = [str(c) for c in self.x]
        return ",".join(s_x)


def unit_vector(i: int, n: int):
    """Return the unit vector of dimension `n` in direction `i`."""
    v: list[float] = [0] * n
    v[i] = 1
    return Vector(v)


def find_delta(fun: Fun, x: Point, i: int):
    """Say if `fun decreases` in the direction `i` or `-i`."""
    delta = unit_vector(i, len(x)) * step
    y0 = fun(x)
    yp = fun(x+delta)
    ym = fun(x-delta)
    if yp <= y0:
        return delta
    if ym <= y0:
        return -delta
    return delta


def v_optimize(fun: Fun, x0: Point, v: Vector) -> Point:
    """Return the minimum of `fun` that one can find in direction `v`."""
    old_x = x0
    new_x = x0 + v
    num = 0
    while fun(new_x) < fun(old_x):
        dprint(f"  opti {v} -> {new_x}")
        num += 1
        old_x = new_x
        new_x = new_x + v
        if num > 10:
            # never more than 10 steps.
            # It could happen that `fun` goes to -infinity
            return new_x
    return new_x


def one_loop(fun: Fun, x0: Point) -> Point:
    """Make one optimization in each direction."""
    new_x = x0
    for i in range(0, len(x0)):
        v = find_delta(fun, new_x, i)
        dprint(f"direction {i}: vecteur={v}")
        new_x = v_optimize(fun, new_x, v)
    return new_x


def find_min(fun: Fun, x0: Point):
    """Find local min from x0."""
    y0 = fun(x0)
    dprint(f"départ: f({x0})={y0}")

    new_x = x0
    for num in range(1, 100):
        print(f"loop n {num}")
        print("----------------------")
        old_x = new_x
        new_x = one_loop(fun, new_x)
        new_y = fun(new_x)
        dprint(f"après {num} tours on a : f({new_x})={new_y}")
        if abs(fun(old_x)-fun(new_x)) < epsilon:
            return new_x
    return new_x
