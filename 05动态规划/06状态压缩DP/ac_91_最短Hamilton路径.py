MAX_INF = 10**18
def main():
    n = int(input())
    dis = [list(map(int, input().split())) for _ in range(n)]

    f = [[MAX_INF] * (n + 1) for _ in range(1 << n)]
    f[1][0] = 0
    for i in range(1, 1 << n):
        for j in range(n):
            if i >> j & 1 == 1:
                for k in range(n):
                    if ((i ^ (1<<j)) >> k & 1) ==1:
                        f[i][j] = min(f[i ^ (1 << j)][k] + dis[k][j], f[i][j])

    print(f[(1<<n) - 1][n - 1])
if __name__ == "__main__":
    main()