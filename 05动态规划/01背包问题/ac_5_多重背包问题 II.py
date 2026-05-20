def main():
    n, m = map(int, input().split())
    vws = [list(map(int, input().split())) for _ in range(n)]

    vw = []
    for (v,w,s) in vws:
        j = 1
        while s >= j:
            vw.append([v * j, w * j])
            s -= j
            j *= 2

        if s > 0:
            vw.append([v * s, w * s])

    dp = [0] * (m + 1)

    for (v,w) in vw:
            for i in range(m, v- 1, -1):
                dp[i] = max(dp[i], dp[i - v] + w)

    print(dp[m])

if __name__ == "__main__":
    main()