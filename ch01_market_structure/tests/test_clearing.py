from ch01_market_structure.src.clearing import MarginAccount, FuturesPosition


def test_futures_daily_pnl_long():
    pos = FuturesPosition(contracts=2, contract_multiplier=1000, prev_price=100.0)
    pnl = pos.daily_pnl(new_price=101.5)
    assert pnl == 2 * 1000 * 1.5


def test_margin_call_trigger():
    acct = MarginAccount(balance=8000, initial_margin=10000, maintenance_margin=8500)
    # balance < maintenance => margin call to restore to initial
    assert acct.margin_call_amount() == 2000


def test_no_margin_call_when_above_maintenance():
    acct = MarginAccount(balance=9000, initial_margin=10000, maintenance_margin=8500)
    assert acct.margin_call_amount() == 0
