def main():
    n, m = map(int, input().split())
    ss = input()

    MOD = 2 ** 64
    p = [1] * (n + 1)
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        f[i] = (f[i - 1] * 131 + ord(ss[i - 1])) % MOD
        p[i] = p[i - 1] * 131 % MOD

    def _get(l, r: int) -> int:
        return (f[r] - f[l -1] * p[r - l + 1]) % MOD

    for _ in range(m):
        l1,r1,l2,r2 = map(int, input().split())
        print(
            "Yes" if _get(l1,r1) == _get(l2,r2) else "No"
        )

if __name__ == "__main__":
    main()