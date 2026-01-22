from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class DerivativeExposure:
    notional: float
    mtm: float  # current mark-to-market (market value)

    @property
    def mtm_to_notional(self) -> float:
        if self.notional == 0:
            return 0.0
        return self.mtm / self.notional


def toy_fx_forward_example(notional: float = 100_000_000.0, mtm: float = 1_000_000.0) -> DerivativeExposure:
    """
    Simple illustration: large notional, relatively small current MTM.
    Used to reinforce the Ch.1 point that notional is not the same as value-at-risk today.
    """
    return DerivativeExposure(notional=notional, mtm=mtm)
