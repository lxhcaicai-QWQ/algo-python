
def main():
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))
    n = len(arr)
    sums = [0] * (n + 1)
    for i in range(n):
        sums[i + 1] = sums[i] + arr[i]

    def _query(l, r: int):
        return sums[r] - sums[l-1]

    for _ in range(m):
        l, r = map(int, input().split())
        print(_query(l, r))

if __name__ == "__main__":
    main()