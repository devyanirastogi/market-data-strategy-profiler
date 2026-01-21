import csv
from datetime import datetime
from typing import List
from models import MarketDataPoint

def load_market_data(csv_path: str) -> List[MarketDataPoint]:
    """
    Adapt Apple CSV (Date,Price,...) -> timestamp,symbol,price
    Time: O(n), Space: O(n)
    """
    data = []
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row_num, row in enumerate(reader, 1):
            try:
                date_str = row[0].strip('"')  # "01/20/2026"
                price_str = row[1].strip('"')  # "246.75"
                
                # Parse MM/DD/YYYY -> datetime
                timestamp = datetime.strptime(date_str, '%m/%d/%Y')
                price = float(price_str)
                
                point = MarketDataPoint(timestamp, 'AAPL', price)
                data.append(point)
            except (ValueError, IndexError):
                print(f"Skipping invalid row {row_num}: {row}")
                continue
    
    print(f"Loaded {len(data)} ticks")
    return data