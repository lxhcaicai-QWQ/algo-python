def main():
    n, m = map(int, input().split())

    c = []
    v = []
    w = []
    for _ in range(n):
        c.append(int(input()))
        v.append([])
        w.append([])
        for _ in range (c[-1]):
            a,b = map(int, input().split())
            v[-1].append(a)
            w[-1].append(b)

    dp = [0] * (m +1)
    for i in range(n):
        for j in range(m, -1, -1):
            for k in range(c[i]):
                if j >= v[i][k]:
                    dp[j] = max(dp[j], dp[j-v[i][k]] + w[i][k])

    print(dp[m])

if __name__ == "__main__":
    main()