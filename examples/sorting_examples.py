from complexitylab.analyzer import analyze

def bubble_sort(arr):
    arr = arr[:]  # copy to avoid modifying input
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def gen_reverse(n):
    return list(range(n, 0, -1))

if __name__ == "__main__":
    sizes = [100, 200, 400]
    results = analyze(bubble_sort, gen_reverse, sizes)
    for r in results:
        print(r)
