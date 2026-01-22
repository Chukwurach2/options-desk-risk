from __future__ import annotations
from dataclasses import dataclass


@dataclass
class MarginAccount:
    balance: float
    initial_margin: float
    maintenance_margin: float

    def apply_variation_margin(self, pnl: float) -> None:
        """Daily settlement: add/subtract daily P&L."""
        self.balance += pnl

    def margin_call_amount(self) -> float:
        """
        If balance falls below maintenance, top back up to initial margin.
        """
        if self.balance < self.maintenance_margin:
            return self.initial_margin - self.balance
        return 0.0


@dataclass
class FuturesPosition:
    contracts: int          # positive = long, negative = short
    contract_multiplier: float
    prev_price: float       # yesterday's futures price

    def daily_pnl(self, new_price: float) -> float:
        """
        Daily futures P&L = (# contracts) * multiplier * (price change).
        """
        pnl = self.contracts * self.contract_multiplier * (new_price - self.prev_price)
        self.prev_price = new_price
        return pnl
