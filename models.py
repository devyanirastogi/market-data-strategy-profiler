from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class MarketDataPoint:
    """Immutable market tick. Space: O(1) per point, O(n) for list."""
    timestamp: datetime
    symbol: str
    price: float

class Strategy(ABC):
    @abstractmethod
    def generate_signals(self, tick: MarketDataPoint) -> list:
        """Returns ['BUY'] or ['SELL'] or []."""
        pass
