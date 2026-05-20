def main():
    n, m = map(int, input().split())
    vws = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (m + 1)

    for (v,w,s) in vws:
        for _ in range(s):
            for i in range(m, v- 1, -1):
                dp[i] = max(dp[i], dp[i - v] + w)

    print(dp[m])

if __name__ == "__main__":
    main()