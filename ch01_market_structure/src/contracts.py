from __future__ import annotations
from dataclasses import dataclass
from typing import Literal, Union

Position = Literal["long", "short"]


@dataclass(frozen=True)
class ForwardContract:
    K: float  # delivery price


@dataclass(frozen=True)
class EuropeanCall:
    K: float


@dataclass(frozen=True)
class EuropeanPut:
    K: float


Contract = Union[ForwardContract, EuropeanCall, EuropeanPut]


def payoff(contract: Contract, ST: float, position: Position = "long") -> float:
    """
    Payoff at maturity for basic Chapter 1 contracts.
    (Pricing comes later; this is pure payoff mechanics.)
    """
    if isinstance(contract, ForwardContract):
        val = ST - contract.K
    elif isinstance(contract, EuropeanCall):
        val = max(ST - contract.K, 0.0)
    elif isinstance(contract, EuropeanPut):
        val = max(contract.K - ST, 0.0)
    else:
        raise TypeError("Unsupported contract type")

    return val if position == "long" else -val
