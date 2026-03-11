class FuturesContract:
    """
    Basic representation of a futures contract.
    """

    def __init__(self, underlying, contract_size, entry_price, position="long"):
        self.underlying = underlying
        self.contract_size = contract_size
        self.entry_price = entry_price
        self.position = position.lower()

    def pnl(self, current_price):
        """
        Calculate profit/loss given a new futures price.
        """
        price_change = current_price - self.entry_price

        if self.position == "long":
            return price_change * self.contract_size
        elif self.position == "short":
            return -price_change * self.contract_size
        else:
            raise ValueError("Position must be 'long' or 'short'")

    def __repr__(self):
        return (
            f"FuturesContract("
            f"{self.position} {self.contract_size} units of {self.underlying} "
            f"@ {self.entry_price})"
        )
