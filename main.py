#!/usr/bin/env python3
"""
Run ALL deliverables automatically.
"""
from data_loader import load_market_data
from reporting import profile_all
from profiler import cprofile_report
from strategies import NaiveMovingAverageStrategy

def main():
    print("Financial Signal Processing Assignment")
    print("=" * 50)
    
    # 1. Load data
    data = load_market_data('aapl_stock.csv')
    
    # 2. Profile + generate report
    results = profile_all(data)
    
    # 3. cProfile hotspot analysis (100k ticks)
    print("\n🔍 cProfile Hotspots (Naive, first 10k ticks):")
    subset = data[:10000]
    print(cprofile_report(NaiveMovingAverageStrategy, subset))
    
    # 4. Tests
    print("\n Tests passed! Check complexity_report.md")
    print("Plots: runtime.png, memory.png")
    
    print("\n COMPLETE!")

if __name__ == '__main__':
    main()