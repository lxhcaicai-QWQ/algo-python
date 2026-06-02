def main():
    MOD = 10 ** 9 + 7
    N = 2010
    c = [[0] * (N + 1) for _ in range(N + 1)]
    def _calculate():
        for i in range(0, N + 1):
            for j in range(0, i + 1):
                if j == 0:
                    c[i][j] = 1
                else:
                    c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD

    _calculate()
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        print(c[a][b])

if __name__ == "__main__":
    main()