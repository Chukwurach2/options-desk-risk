from ch03_futures_hedging.src.cross_hedge import cross_hedge_contracts


def test_cross_hedge_contracts():
    result = cross_hedge_contracts(
        exposure_units=100_000,
        futures_contract_size=25_000,
        rho=0.9,
        sigma_s=0.03,
        sigma_f=0.025,
    )
    assert "hedge_ratio" in result
    assert "contracts" in result
    assert result["contracts"] > 0
