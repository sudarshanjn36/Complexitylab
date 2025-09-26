import time
import tracemalloc

def analyze(func, generator, sizes):
    """
    Run func(generator(n)) for each n in sizes.
    Measure runtime and memory.
    """
    results = []
    for n in sizes:
        data = generator(n)

        tracemalloc.start()
        start = time.perf_counter_ns()
        func(data)
        end = time.perf_counter_ns()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        results.append({
            "n": n,
            "time_s": (end - start) / 1e9,
            "mem_bytes": peak
        })
    return results
