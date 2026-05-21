N = 10 ** 10
def main():
    n = int(input())
    nums = list(map(int, input().split()))
    sums = [0] * (n + 1)
    for i in range(1, n + 1):
        sums[i] = sums[i - 1] + nums[i - 1]

    f = [[N] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        f[i][i] = 0
    for length in range(1, n + 1):
        for i in range(1, n - (length - 1) + 1):
            j = i + length - 1
            for k in range(i, j):
                f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j] + sums[j] - sums[i - 1])
    print(f[1][n])
if __name__ == "__main__":
    main()