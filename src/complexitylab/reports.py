def print_table(results):
    print(f"{'n':<8}{'time(s)':<12}{'mem(bytes)':<12}")
    for r in results:
        print(f"{r['n']:<8}{r['time_s']:<12.6f}{r['mem_bytes']:<12}")


def print_fit(best, allfits):
    print("\nComplexity Fit Results:")
    print(f"Best Fit: {best[0]} (error={best[1]:.2e})")
    print("\nAll Fits (sorted):")
    for label, err in allfits:
        print(f"{label:<10} error={err:.2e}")
