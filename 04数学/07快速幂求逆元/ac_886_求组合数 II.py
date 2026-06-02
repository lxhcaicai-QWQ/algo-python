def main():
    MOD = 10 ** 9 + 7
    N = 10 ** 5 + 10

    def _ksm(a, b: int) -> int:
        a %= MOD
        res = 1
        while b!=0:
            if b & 1 == 1:
                res = res * a % MOD
            a = a * a % MOD
            b >>= 1
        return res

    fac = [1] * N
    inf = [1] * N
    def _init():
        for i in range(1, N):
            fac[i] = fac[i - 1] * i % MOD
            inf[i] = inf[i-1] * _ksm(i, MOD - 2) % MOD

    _init()
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        print(fac[a] * inf[b] % MOD * inf[a - b] % MOD)

if __name__ == "__main__":
    main()