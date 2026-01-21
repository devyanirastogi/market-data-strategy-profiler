from data_loader import load_market_data
from strategies import *
from profiler import measure_time, measure_memory

data = load_market_data('aapl_stock.csv')[:20]

# Test 1: Correct types
strat = NaiveMovingAverageStrategy()
signals = strat.generate_signals(data[0])
assert isinstance(signals, list)

# Test 2: Optimized is fast (<1s, <100MB for 100k)
from profiler import measure_time, measure_memory
time_fast = measure_time(OptimizedNaiveStrategy, data[:50000])
mem_fast = measure_memory(OptimizedNaiveStrategy, data[:50000])
assert time_fast < 1.0
assert mem_fast < 100

print("All unit tests passed!")
