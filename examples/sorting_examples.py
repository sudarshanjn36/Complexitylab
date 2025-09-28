from complexitylab.analyzer import analyze
from complexitylab.fitting import fit_curves
from complexitylab.reports import print_table, print_fit


def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def gen_reverse(n):
    return list(range(n, 0, -1))


if __name__ == "__main__":
    sizes = [100, 200, 400]
    results = analyze(bubble_sort, gen_reverse, sizes)

    print_table(results)

    ns = [r["n"] for r in results]
    times = [r["time_s"] for r in results]

    best, allfits = fit_curves(ns, times)
    print_fit(best, allfits)
