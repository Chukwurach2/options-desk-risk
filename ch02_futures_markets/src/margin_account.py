class MarginAccount:
    """
    Simulates a futures margin account.
    """

    def __init__(self, initial_margin, maintenance_margin):
        self.initial_margin = initial_margin
        self.maintenance_margin = maintenance_margin
        self.balance = initial_margin

    def mark_to_market(self, pnl):
        """
        Apply daily PnL to margin balance.
        """
        self.balance += pnl

        if self.balance < self.maintenance_margin:
            return self.margin_call()

        return 0

    def margin_call(self):
        """
        Amount needed to restore balance to initial margin.
        """
        call_amount = self.initial_margin - self.balance
        self.balance = self.initial_margin
        return call_amount

    def __repr__(self):
        return f"MarginAccount(balance={self.balance})"
