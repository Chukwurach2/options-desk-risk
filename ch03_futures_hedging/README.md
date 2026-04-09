# Chapter 3 — Hedging with Futures (Hull 11e)

This chapter artifact implements core hedging mechanics using futures:

- Short and long hedge intuition
- Minimum-variance hedge ratio
- Basis risk and hedge effectiveness
- Cross-hedging logic
- Stack-and-roll exposure over time

Chapter 3 focuses on how futures can be used to reduce price risk, while recognizing that real hedges are rarely perfect because of basis risk and contract mismatch

## Why this matters for desk risk

For risk teams, hedging is not just about directionally offsetting exposure. It is about:

- sizing the hedge correctly
- understanding residual basis risk
- tracking hedge performance through time
- managing roll risk when short-dated contracts are used repeatedly

These mechanics show up across commodities, rates, FX, and equity index overlays.

## Contents

- `notes.md` — concise notes summarizing the chapter concepts
- `src/hedge_ratio.py` — minimum-variance hedge ratio and contract sizing
- `src/basis_risk.py` — basis calculations and hedge P&L decomposition
- `src/cross_hedge.py` — cross-hedging utilities using correlation and vol inputs
- `src/stack_and_roll.py` — simple stack-and-roll hedge simulation
- `tests/` — unit tests for hedge mechanics

## Concepts Practiced in Code

- long vs short hedge setup
- hedge ratio estimation
- basis risk
- cross-hedging
- stack-and-roll intuition
