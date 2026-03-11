from src.futures_contract import FuturesContract


def test_long_pnl():
    contract = FuturesContract("Oil", 1000, 70, "long")

    pnl = contract.pnl(72)

    assert pnl == 2000


def test_short_pnl():
    contract = FuturesContract("Oil", 1000, 70, "short")

    pnl = contract.pnl(68)

    assert pnl == 2000
