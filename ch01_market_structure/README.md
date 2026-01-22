# Chapter 1 — Market Structure (Hull 11e, pp. 23–41)

This chapter artifact implements small, testable pieces of market-structure logic:
- Contract payoffs (forward/futures/options)
- Clearinghouse mechanics (margin + daily settlement / marking-to-market)
- OTC vs exchange-traded measurement intuition (notional vs market value)

## Why this matters for desk risk
A large fraction of “derivatives blow-ups” are driven by:
- leverage + funding/margin dynamics,
- liquidity and forced unwinds,
- operational mechanics (how positions are settled and collateralized),
not just pricing models.

## Contents
- `src/contracts.py` — payoff functions and position representation
- `src/clearing.py` — a simple clearinghouse + margin account simulator
- `src/market_size.py` — notional vs MTM examples
- `tests/` — unit tests for core mechanics
