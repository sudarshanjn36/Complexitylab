from complexitylab.analyzer import analyze
from complexitylab.reports import print_table, print_fit
from complexitylab.fitting import fit_curves


# Stack Implementation
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0


# Function to test (Push all elements, then Pop all elements)
def stack_ops(n):
    s = Stack()
    # Push n elements
    for i in range(n):
        s.push(i)
    # Pop all elements
    while not s.isEmpty():
        s.pop()
    return True


# Input generator (just numbers up to n)
def gen_range(n):
    return n


if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10000]

    # analyze stack_ops (we don’t really need data, just n)
    results = analyze(lambda n: stack_ops(n), gen_range, sizes)

    print_table(results)

    ns = [r["n"] for r in results]
    times = [r["time_s"] for r in results]

    best, allfits = fit_curves(ns, times)
    print_fit(best, allfits)
# few changes that has been made in the code ("I have changed example from sorting to stack verification")