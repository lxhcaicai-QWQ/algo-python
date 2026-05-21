def main():
    n = int(input())
    f = [0] * (n + 1)
    f[0] = 1
    MOD = 10 ** 9 + 7
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            f[j] += f[j - i]
            f[j] %= MOD

    print(f[n])

if __name__ == "__main__":
    main()