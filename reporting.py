import matplotlib.pyplot as plt
import pandas as pd
from typing import List, Dict
from data_loader import load_market_data  
from strategies import * 
from profiler import measure_time, measure_memory, cprofile_report

def generate_report(results: List[Dict], filepath: str):
    """Create plots + markdown."""
    
    df = pd.DataFrame(results)
    
    # Plot 1: Runtime
    plt.figure(figsize=(10, 5))
    for strat in df['strategy'].unique():
        subset = df[df['strategy'] == strat]
        plt.plot(subset['n'], subset['time'], 'o-', label=strat)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Input Size (ticks)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime vs Input Size')
    plt.legend()
    plt.savefig('runtime.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    # Plot 2: Memory  
    plt.figure(figsize=(10, 5))
    for strat in df['strategy'].unique():
        subset = df[df['strategy'] == strat]
        plt.plot(subset['n'], subset['memory'], 'o-', label=strat)
    plt.xscale('log')
    plt.xlabel('Input Size (ticks)')
    plt.ylabel('Peak Memory (MiB)')
    plt.title('Memory vs Input Size')
    plt.legend()
    plt.savefig('memory.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    # Markdown report
    with open(filepath, 'w') as f:
        f.write('# Complexity Analysis Report\n\n')
        
        f.write('## Performance Table\n\n')
        f.write("| Strategy | n | Time(s) | Memory(MB) |\n")
        f.write("|----------|---|---------|------------|\n")
        for _, row in df.iterrows():
            f.write(f"| {row['strategy']:8} | {int(row['n']):,} | {row['time']:.4f} | {row['memory']:.1f} |\n")

        f.write('\n\n')
        
        f.write('## Plots\n')
        f.write('![Runtime](runtime.png)\n\n')
        f.write('![Memory](memory.png)\n\n')
        
        f.write('## Complexity Summary\n\n')
        f.write('| Strategy | Time | Space |\n')
        f.write('|----------|------|-------|\n')
        f.write('| Naive | O(n²) | O(n) |\n')
        f.write('| Windowed | O(n) | O(k) |\n')
        f.write('| Optimized | O(n) | O(1) |\n\n')
        
        f.write('## Analysis\n')
        f.write('- **Naive**: Quadratic runtime due to repeated summation.\n')
        f.write('- **Windowed**: Linear time, constant space (window size).\n')
        f.write('- **Optimized**: Linear time, constant space (running sum).\n')

def profile_all(data):
    """Benchmark all strategies."""
    sizes = [1000, 10000, 50000][:len(data)]  # adapt to your data size
    results = []
    
    strategies = {
        'naive': NaiveMovingAverageStrategy,
        'windowed': lambda: WindowedMovingAverageStrategy(10),
        'optimized': OptimizedNaiveStrategy
    }
    
    for n in sizes:
        subset = data[:n]
        for name, strat_cls in strategies.items():
            time_s = measure_time(strat_cls, subset)
            mem_mb = measure_memory(strat_cls, subset)
            
            results.append({
                'strategy': name,
                'n': n,
                'time': time_s,
                'memory': mem_mb
            })
            
            print(f"{name:10} n={n:5,} time={time_s:.4f}s mem={mem_mb:.1f}MB")
    
    generate_report(results, 'complexity_report.md')
    return results
