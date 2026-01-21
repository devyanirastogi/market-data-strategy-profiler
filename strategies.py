from typing import List
from collections import deque
from models import MarketDataPoint, Strategy

class NaiveMovingAverageStrategy(Strategy):
    """
    Recomputes average from ALL past prices each tick.
    Time per tick: O(t) where t=history length → Overall: O(n²)
    Space: O(n) for full history list
    """
    def __init__(self):
        self.prices = []  # O(n) space

    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        self.prices.append(tick.price)  # O(1)
        
        # O(t) recompute - bottleneck!
        avg = sum(self.prices) / len(self.prices)
        
        if tick.price > avg * 1.001:    # 0.1% threshold
            return ["BUY"]
        elif tick.price < avg * 0.999:
            return ["SELL"]
        return []

class WindowedMovingAverageStrategy(Strategy):
    """
    Fixed window + running sum. Time: O(1) per tick → O(n) overall
    Space: O(k) where k=window_size
    """
    def __init__(self, window_size: int = 10):
        self.window = deque(maxlen=window_size)
        self.window_sum = 0.0

    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        # O(1) updates
        if len(self.window) == self.window.maxlen:
            self.window_sum -= self.window[0]
        
        self.window.append(tick.price)
        self.window_sum += tick.price
        
        avg = self.window_sum / len(self.window)
        
        if tick.price > avg * 1.001:
            return ["BUY"]
        elif tick.price < avg * 0.999:
            return ["SELL"]
        return []

class OptimizedNaiveStrategy(Strategy):
    """
    OPTIMIZATION: Running sum instead of recomputing.
    Time: O(1) per tick → O(n) overall
    Space: O(1) - just two numbers!
    """
    def __init__(self):
        self.count = 0
        self.running_sum = 0.0

    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        self.count += 1
        self.running_sum += tick.price  # O(1)
        
        avg = self.running_sum / self.count  # O(1)
        
        if tick.price > avg * 1.001:
            return ["BUY"]
        elif tick.price < avg * 0.999:
            return ["SELL"]
        return []