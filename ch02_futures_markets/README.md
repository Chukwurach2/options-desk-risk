# Chapter 2 — Futures Markets and Central Counterparties (Hull 11e)

This chapter artifact implements the operational mechanics of futures markets:

- Contract specifications
- Margin accounts and daily settlement
- Clearinghouse structure and counterparty risk
- Futures–spot convergence and basic arbitrage intuition

Futures contracts are standardized derivatives traded on exchanges where a clearinghouse stands between counterparties and guarantees performance. Margin accounts and daily mark-to-market settlement significantly reduce default risk compared to OTC derivatives. 

## Why this matters for desk risk

For risk teams and derivatives desks, futures markets introduce several practical mechanics:

- **Margin dynamics** drive liquidity risk and forced unwinds
- **Daily settlement (mark-to-market)** continuously realizes PnL
- **Clearinghouses** transform bilateral credit exposure into centrally managed risk
- **Futures–spot convergence** creates arbitrage relationships near delivery

Understanding these mechanics is critical when monitoring leverage, liquidity stress, and trading exposure.

## Contents

- `notes.md` — summarizing the chapter concepts
- `src/futures_contract.py` — representation of futures contract specifications
- `src/margin_account.py` — simulation of initial margin, maintenance margin, and margin calls
- `src/clearinghouse.py` — simplified CCP structure between counterparties
- `src/convergence.py` — simple model illustrating futures–spot convergence
- `tests/` — unit tests validating core mechanics

## Concepts Practiced in Code

Key mechanics explored in the code artifacts include:

- Futures contract structure (underlying, contract size, delivery)
- Daily marking-to-market
- Margin calls and account balance updates
- Clearinghouse intermediation
- Convergence of futures prices to spot prices near delivery
