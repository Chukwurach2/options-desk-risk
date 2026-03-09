# Hull Ch. 2 (pp 46 - 67)

## Futures contract structure
- Futures are standardized exchange-traded contracts specifying an asset, contract size, delivery date(s), and price quotation.
- Exchanges define delivery procedures, trading hours, price limits, and position limits to maintain orderly markets.
- Most futures positions are closed before delivery; the possibility of delivery anchors pricing.

## Futures–spot convergence
- As the delivery period approaches, **futures prices converge to the spot price**.
- If futures > spot:
  - short futures
  - buy the asset
  - deliver
- If futures < spot:
  - long futures
  - take delivery
- Arbitrage removes persistent price differences and enforces convergence.

## Margin accounts and daily settlement
- Futures markets use **margin accounts** rather than full contract payment.
- **Initial margin**: collateral posted to open a position.
- **Maintenance margin**: minimum balance required in the account.
- If the balance falls below maintenance margin, a **margin call** requires additional funds.
- Positions are **marked to market daily**, meaning gains and losses are realized continuously rather than at maturity.

## Clearinghouses / central counterparties (CCPs)
- Clearinghouses stand between buyers and sellers:
  
  trader → clearinghouse → trader

- They guarantee contract performance and manage margin flows.
- This structure converts bilateral credit exposure into centrally managed risk.

## Risk transformation
- CCP clearing reduces **counterparty credit risk**, but introduces **liquidity risk** through margin requirements.
- During large market moves, variation margin can create sudden cash needs for leveraged traders.

## Contract specifications and market mechanics
Exchanges define key parameters:

- contract size
- delivery months
- price quotation conventions
- price limits (daily movement caps)
- position limits (max contracts held)

These rules help maintain liquidity and prevent market manipulation.

## Delivery and settlement
- Some futures require **physical delivery** of the underlying asset.
- Others use **cash settlement** (e.g., stock index futures).
- In practice, traders usually offset positions before delivery.

## Forward vs futures intuition
Key differences:

- **Futures**
  - exchange traded
  - standardized
  - daily settlement
  - clearinghouse guarantees trades

- **Forwards**
  - OTC contracts
  - customizable terms
  - settled at maturity
  - bilateral counterparty risk

## Risk perspective
Operational mechanics of futures markets create several important risk dynamics:

- leverage from margining
- forced liquidation due to margin calls
- liquidity shocks during large price moves
- CCP concentration of systemic risk
