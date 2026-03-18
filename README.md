# 📊 Market Data Strategy Profiler

This project is a small quantitative research tool I built to explore how different trading strategies perform on historical market data.

The goal wasn’t to create a production trading system, but to understand the full workflow behind strategy development; from working with raw financial data to testing and comparing ideas in a structured way.

## About The Project
At its core, the project takes historical market data, applies a set of rule-based trading strategies, and evaluates how those strategies would have performed over time.

It follows a simple pipeline:
- Load and clean historical price data
- Apply trading strategies (e.g. trend-following or momentum-style rules)
- Simulate trades over a chosen time period
- Track performance and compare results across strategies

The “profiler” aspect comes from looking beyond just total returns and trying to understand how each strategy behaves over time.

## Why I built this
I wanted to go beyond just learning financial theory and actually build something hands-on. 
This project helped me understand:
- How trading strategies are structured in code
- How backtesting works (and its limitations)
- Why comparing strategies requires more than just looking at profit

It also made it clear how easy it is to overestimate a strategy’s performance without proper validation.

## What’s included
- A basic data pipeline for handling time-series market data
- A framework for defining and testing multiple strategies
- A backtesting setup to simulate trades
- Performance tracking to compare outcomes across strategies

The code is organized so that new strategies can be added without changing the rest of the system.

## Limitations
This project is intentionally simple and comes with a few important limitations:
- It assumes ideal trade execution (no slippage or transaction costs)
- Strategies are based mostly on technical indicators
- There’s no out-of-sample or walk-forward validation
- It focuses on single-asset backtesting rather than full portfolios

Because of this, the results should be seen as exploratory rather than predictive.

## Further Improvements
If I were to keep building on this, the main areas I’d focus on are:

- Making the backtesting more realistic by adding transaction costs and position sizing
- Introducing proper validation (train/test splits, walk-forward testing)
- Expanding to multiple assets and portfolio-level analysis
- Experimenting with machine learning models instead of fixed rules
- Building a simple dashboard to visualize strategy performance

## Tech stack
This project was built using Python, mainly with pandas and NumPy for data handling, along with basic visualization tools.

## Final thoughts
This project was a way for me to explore quantitative finance in a practical way. It’s not meant to “beat the market,” but rather to understand how strategies are built, tested, and evaluated — and where things can go wrong. 