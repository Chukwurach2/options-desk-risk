import numpy as np


def simulate_convergence(spot_price, futures_price, days):
    """
    Simulate futures price converging to spot price as expiration approaches.
    """

    futures_path = []

    for t in range(days, 0, -1):
        adjustment = (spot_price - futures_price) / t
        futures_price += adjustment
        futures_path.append(futures_price)

    return np.array(futures_path)
