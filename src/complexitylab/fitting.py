import math


CANDIDATES = {
    "O(1)": lambda n: 1,
    "O(log n)": lambda n: math.log(n + 1),
    "O(n)": lambda n: n,
    "O(n log n)": lambda n: n * math.log(n + 1),
    "O(n^2)": lambda n: n ** 2,
    "O(n^3)": lambda n: n ** 3,
    "O(2^n)": lambda n: 2 ** n if n< 30 else float("inf"), 
}

def fit_curves(ns, times):

    results = []
    
    for label, func in CANDIDATES.items():
        predicted = [func(n) for n in ns]
        scale = sum(t * p for t, p in zip(times, predicted)) / sum(p * p for p in predicted)

        error = sum((t - scale * p ) ** 2 for t, p in zip(times, predicted))
        results.append((label, error))

    results.sort(key = lambda x:x[1])
    best = results[0]
    
    return best, results