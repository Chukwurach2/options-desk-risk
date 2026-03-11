class ClearingHouse:
    """
    Simplified clearinghouse that intermediates futures trades.
    """

    def __init__(self):
        self.positions = []

    def register_trade(self, long_trader, short_trader, contract):
        """
        Clearinghouse becomes counterparty to both sides.
        """
        self.positions.append({
            "long": long_trader,
            "short": short_trader,
            "contract": contract
        })

    def mark_to_market(self, new_price):
        """
        Apply PnL to all contracts.
        """
        results = []

        for trade in self.positions:
            contract = trade["contract"]
            pnl = contract.pnl(new_price)

            results.append({
                "long_trader": trade["long"],
                "short_trader": trade["short"],
                "pnl": pnl
            })

        return results
