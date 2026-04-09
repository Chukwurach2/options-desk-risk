from ch03_futures_hedging.src.hedge_ratio import (
    minimum_variance_hedge_ratio,
    optimal_contracts,
    hedge_direction,
)


def test_minimum_variance_hedge_ratio():
    h = minimum_variance_hedge_ratio(rho=0.8, sigma_s=0.025, sigma_f=0.02)
    assert round(h, 4) == 1.0


def test_optimal_contracts():
    n = optimal_contracts(exposure_units=2_000_000, futures_contract_size=42_000, hedge_ratio=0.78)
    assert n == round(0.78 * 2_000_000 / 42_000)


def test_hedge_direction():
    assert hedge_direction("long_asset") == "short_futures"
    assert hedge_direction("future_purchase") == "long_futures"
