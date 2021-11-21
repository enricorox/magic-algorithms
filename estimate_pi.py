"""
Monte Carlo Algorithm to estimate PI
"""

import math
import random
import sys

from sympy import N

NUM_DEC_DIGITS = 2
CORRECTNESS = 95


def mc_loop(epsilon, delta):
    """
    Use Monte Carlo counting to estimate PI

    :param epsilon: precision
    :param delta: confidence
    :return: number of point in the circle, total number of point
    """
    # number of point needed
    k = math.ceil(4*math.log(2/delta)/epsilon**2)
    print(f"Going to generate {k} points...")

    # point in circle counter
    count = 0

    for i in range(1, k):
        x = random.uniform(-1, +1)
        y = random.uniform(-1, +1)
        if x ** 2 + y ** 2 <= 1:
            count += 1

        # completion bar (it does not print on some IDEs)
        if i % 1000000 == 0:
            print(f" [ completed {(i/k*100): 2.2f}% ]", end='\r')

    print(" [ completed 100.00% ] ")
    return count, k


def estimate_pi(digits: int, correctness: float):
    """
    Estimate PI as an (epsilon, delta)-approximation

    :param digits: number of decimal digit to compute
    :param correctness: percentage of correctness
    :return: PI with given decimal digit
    """
    epsilon = (10 ** -digits) / 3
    delta = 1 - correctness / 100
    print(f"We will find a ({epsilon: .4f}, {delta: .4f})-approximation")
    count, k = mc_loop(epsilon, delta)
    factor = 10 ** digits
    return math.trunc((4 * count) / k * factor) / factor


if __name__ == '__main__':
    if len(sys.argv) > 1:
        dig = int(sys.argv[1])
    else:
        dig = NUM_DEC_DIGITS

    pi = estimate_pi(dig, CORRECTNESS)
    print(f"PI = {pi}")
