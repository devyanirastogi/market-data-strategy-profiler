import time
import cProfile
import pstats
import io
import psutil
import os
from typing import Type
from models import Strategy
from strategies import *

def get_process_memory() -> float:
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 ** 2

def run_strategy(strategy: Strategy, data):
    for tick in data:
        strategy.generate_signals(tick)

def measure_time(strategy_cls: Type[Strategy], data):
    """Wall-clock time."""
    strat = strategy_cls()
    start = time.perf_counter()
    run_strategy(strat, data)
    return time.perf_counter() - start

def measure_memory(strategy_cls: Type[Strategy], data):
    mem_before = get_process_memory()
    strat = strategy_cls()
    run_strategy(strat, data)
    mem_after = get_process_memory()
    return mem_after - mem_before + 20  # baseline overhead

def cprofile_report(strategy_cls: Type[Strategy], data):
    strat = strategy_cls()
    pr = cProfile.Profile()
    pr.enable()
    run_strategy(strat, data)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumtime')
    ps.print_stats(5)
    return s.getvalue()