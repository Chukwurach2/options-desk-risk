from ch03_futures_hedging.src.basis_risk import basis, hedge_pnl_short_hedge


def test_basis():
    assert basis(100, 98) == 2


def test_short_hedge_pnl():
    result = hedge_pnl_short_hedge(
        spot_entry=50,
        spot_exit=45,
        futures_entry=49,
        futures_exit=45,
        quantity=1_000,
    )
    assert result["spot_pnl"] == -5000
    assert result["futures_pnl"] == 4000
    assert result["total_pnl"] == -1000
