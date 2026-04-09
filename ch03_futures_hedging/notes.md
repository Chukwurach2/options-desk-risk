# Hull Ch. 3 Notes — Hedging Strategies Using Futures

## Basic hedge intuition
- A **short hedge** is used when you own an asset, or expect to own it, and want protection against a price decline.
- A **long hedge** is used when you will need to buy an asset later and want protection against a price increase.
- A perfect hedge is rare; most real hedges leave some residual risk.

## Why hedging is imperfect
- The main source of imperfection is **basis risk**.
- Basis is typically defined as:

  basis = spot price − futures price

- If basis changes unexpectedly over the hedge horizon, the hedge will not fully offset spot exposure.

## Minimum-variance hedge ratio
- The hedge ratio determines how large the futures hedge should be relative to the spot exposure.
- The minimum-variance hedge ratio is:

  h* = ρ(σ_s / σ_f)

- This is used to reduce the variance of the combined spot + futures position.

## Cross hedging
- Cross hedging is used when no futures contract exists on the exact asset being hedged.
- The hedge then relies on correlation between the asset exposure and the futures contract being used.
- Better correlation generally means a more effective hedge.

## Stack and roll
- Sometimes firms hedge long-dated exposure with repeated short-dated futures because those contracts are more liquid.
- This is called **stack and roll**.
- It introduces **roll risk** and can create liquidity pressure if futures move adversely before the economic hedge benefit is realized.

## Risk perspective
Important practical hedge questions:
- Is the hedge ratio appropriate?
- How volatile is basis?
- How correlated is the proxy contract?
- What happens when the hedge must be rolled repeatedly?
