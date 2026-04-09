from math import floor


def minimum_variance_hedge_ratio(rho: float, sigma_s: float, sigma_f: float) -> float:
    """
    Minimum-variance hedge ratio:
        h* = rho * (sigma_s / sigma_f)
    """
    if sigma_f == 0:
        raise ValueError("sigma_f must be non-zero")
    return rho * (sigma_s / sigma_f)


def optimal_contracts(
    exposure_units: float,
    futures_contract_size: float,
    hedge_ratio: float,
) -> int:
    """
    Approximate optimal number of futures contracts.
    """
    if futures_contract_size <= 0:
        raise ValueError("futures_contract_size must be positive")
    return round(hedge_ratio * exposure_units / futures_contract_size)


def hedge_direction(exposure_type: str) -> str:
    """
    Return hedge direction for a given exposure.
    exposure_type: 'long_asset' or 'future_purchase'
    """
    mapping = {
        "long_asset": "short_futures",
        "future_purchase": "long_futures",
    }
    if exposure_type not in mapping:
        raise ValueError("exposure_type must be 'long_asset' or 'future_purchase'")
    return mapping[exposure_type]
