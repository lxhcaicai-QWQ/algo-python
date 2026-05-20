def main():
    n = int(input())
    a = [[0] * n  for _ in range(n)]
    dp = [[-10**10] * (n + 1)  for _ in range(n + 1)]
    for i in range(n):
        x = list(map(int, input().split()))
        a[i][: len(a)] = x

    dp[1][1] = a[0][0]
    for i in range(2,n + 1):
        for j in range(1,i + 1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + a[i - 1][j - 1]

    ans = max(dp[n])
    print(ans)

if __name__ == "__main__":
    main()