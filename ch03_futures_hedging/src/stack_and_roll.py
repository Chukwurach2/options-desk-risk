def stack_and_roll_pnl(futures_prices: list[float], contract_size: float, n_contracts: int) -> float:
    """
    Sum cumulative roll P&L from sequential short-dated futures hedges.
    Assumes consecutive prices where each step is one close/reopen transition.
    """
    if len(futures_prices) < 2:
        return 0.0

    pnl = 0.0
    for i in range(len(futures_prices) - 1):
        pnl += (futures_prices[i] - futures_prices[i + 1]) * contract_size * n_contracts
    return pnl
