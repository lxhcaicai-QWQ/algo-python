def main():
    n = int(input())
    a = input()
    m = int(input())
    b = input()

    a = " " + a
    b = " " + b

    f = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        f[i][0] = i
    for j in range(1, m + 1):
        f[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i] == b[j]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1

    print(f[n][m])

if __name__ == "__main__":
    main()