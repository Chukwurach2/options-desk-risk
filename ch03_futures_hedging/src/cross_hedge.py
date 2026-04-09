from .hedge_ratio import minimum_variance_hedge_ratio, optimal_contracts


def cross_hedge_contracts(
    exposure_units: float,
    futures_contract_size: float,
    rho: float,
    sigma_s: float,
    sigma_f: float,
) -> dict:
    """
    Compute hedge ratio and contract count for a cross hedge.
    """
    h_star = minimum_variance_hedge_ratio(rho, sigma_s, sigma_f)
    n_contracts = optimal_contracts(exposure_units, futures_contract_size, h_star)

    return {
        "hedge_ratio": h_star,
        "contracts": n_contracts,
    }
