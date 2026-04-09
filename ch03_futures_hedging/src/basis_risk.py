def basis(spot_price: float, futures_price: float) -> float:
    return spot_price - futures_price


def hedge_pnl_short_hedge(
    spot_entry: float,
    spot_exit: float,
    futures_entry: float,
    futures_exit: float,
    quantity: float,
) -> dict:
    """
    P&L decomposition for a short hedge.
    """
    spot_pnl = (spot_exit - spot_entry) * quantity
    futures_pnl = (futures_entry - futures_exit) * quantity
    total_pnl = spot_pnl + futures_pnl

    return {
        "spot_pnl": spot_pnl,
        "futures_pnl": futures_pnl,
        "total_pnl": total_pnl,
        "basis_entry": basis(spot_entry, futures_entry),
        "basis_exit": basis(spot_exit, futures_exit),
    }


def hedge_pnl_long_hedge(
    spot_entry: float,
    spot_exit: float,
    futures_entry: float,
    futures_exit: float,
    quantity: float,
) -> dict:
    """
    P&L decomposition for a long hedge.
    """
    spot_cost_change = (spot_exit - spot_entry) * quantity
    futures_pnl = (futures_exit - futures_entry) * quantity
    net_effect = spot_cost_change - futures_pnl

    return {
        "spot_cost_change": spot_cost_change,
        "futures_pnl": futures_pnl,
        "net_effect": net_effect,
        "basis_entry": basis(spot_entry, futures_entry),
        "basis_exit": basis(spot_exit, futures_exit),
    }
