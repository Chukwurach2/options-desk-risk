# Chapter 2 — Futures Markets and Central Counterparties

Source: Hull, *Options, Futures, and Other Derivatives (11th Edition)*

This chapter explains how futures markets operate, how contracts are structured, and how clearinghouses reduce counterparty risk.

---

# 1. Background

Futures contracts are standardized agreements traded on exchanges that require the delivery of an asset at a predetermined price and date.

Key characteristics:

- Exchange traded
- Standardized contracts
- Daily settlement through margin accounts
- Clearinghouse guarantees contract performance

Participants typically close out positions before delivery rather than exchanging the physical asset.

---

# 2. Specification of a Futures Contract

A futures exchange defines several specifications:

### Underlying asset
The asset that will be delivered (e.g., crude oil, Treasury bonds, equity index).

### Contract size
Amount of the asset per contract.

Example:
- Crude oil futures = 1,000 barrels

### Delivery month
The month when delivery may occur.

### Price quotation
How the price is quoted.

Example:
- Oil: dollars per barrel
- Treasury bonds: dollars and 32nds

### Price limits
Maximum daily price movement allowed.

### Position limits
Maximum contracts a trader can hold to prevent market manipulation.

---

# 3. Convergence of Futures and Spot Prices

As the delivery date approaches: Futures Price → Spot Price

This occurs because arbitrage eliminates price differences.

If futures > spot:

1. Short futures
2. Buy underlying asset
3. Deliver asset

If futures < spot:

1. Long futures
2. Take delivery

Arbitrage forces prices to converge.

---

# 4. Margin Accounts

Futures contracts use **margin accounts** to manage risk.

### Initial Margin
Deposit required to open a position.

### Maintenance Margin
Minimum balance required in the margin account.

### Margin Call
If balance falls below maintenance margin, the trader must deposit funds.

### Mark-to-Market

Positions are settled **daily**: Daily Gain/Loss = (Today's Futures Price − Yesterday's Price) × Contract Size

This reduces default risk.

---

# 5. Central Counterparties (Clearinghouses)

Clearinghouses act as the intermediary between buyers and sellers.

Instead of: Trader A ↔ Trader B

The structure becomes: Trader A ↔ Clearinghouse ↔ Trader B

The clearinghouse:

- guarantees contract performance
- manages margin
- reduces counterparty risk

---

# 6. OTC Markets

Over-the-counter (OTC) derivatives are privately negotiated contracts.

Differences from futures:

| Feature | Futures | OTC |
|-------|-------|------|
| Trading venue | Exchange | Private |
| Standardization | Standardized | Custom |
| Counterparty risk | Low (clearinghouse) | Higher |
| Settlement | Daily | Usually at maturity |

OTC markets often require collateral to manage credit risk.

---

# 7. Market Quotes

Futures prices are quoted differently depending on the contract.

Examples:

- Commodities → dollars per unit
- Treasury futures → dollars and fractions
- FX futures → USD per unit of foreign currency

---

# 8. Delivery

Although futures allow delivery, most contracts are closed before expiration.

Possible settlement types:

### Physical delivery
Actual asset delivered.

### Cash settlement
Cash payment based on the price difference.

Example:
Stock index futures are cash settled.

---

# 9. Types of Orders

Common futures orders include:

### Market Order
Execute immediately at the best available price.

### Limit Order
Execute only at a specified price or better.

### Stop Order
Execute once the price crosses a specified level.

---

# 10. Regulation

Futures markets in the U.S. are regulated primarily by:

- **Commodity Futures Trading Commission (CFTC)**
- Exchanges (e.g., CME)

Regulation aims to:

- prevent manipulation
- ensure financial stability
- protect market participants

---

# 11. Forward vs Futures Contracts

| Feature | Forward | Futures |
|------|------|------|
| Trading | OTC | Exchange |
| Standardization | Custom | Standardized |
| Settlement | At maturity | Daily mark-to-market |
| Counterparty risk | Higher | Lower |
| Liquidity | Lower | Higher |

---

# Key Takeaways

- Futures contracts are standardized derivatives traded on exchanges.
- Clearinghouses guarantee trades and reduce counterparty risk.
- Margin accounts and daily settlement reduce default risk.
- Futures prices converge to spot prices as delivery approaches.
- Most contracts are closed out before delivery occurs.

---

# Next Topics

Chapter 3 examines how futures contracts are used for **hedging strategies**.
