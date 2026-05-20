def main():
    n, m = map(int, input().split())
    vw = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (m + 1)
    for (v,w) in vw:
        for i in range(v, m + 1, 1):
            dp[i] = max(dp[i], dp[i - v] + w)

    print(dp[m])

if __name__ == "__main__":
    main()