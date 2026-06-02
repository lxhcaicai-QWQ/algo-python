def main():

    def _ksm(a,b,p: int) -> int:
        a %= p
        res = 1
        while b!=0:
            if b & 1 == 1:
                res = res * a % p
            a = a * a % p
            b >>= 1
        return res

    def cal(a, b, p: int) -> int:
        if b > a:
            return 0
        if b > a - b:
            b = a - b
        x = 1
        y = 1
        j = a
        for i in range(1,b + 1):
            y = y * i % p
            x = x * j % p
            j -= 1

        return x * _ksm(y, p - 2, p) % p

    def _lucas(n, m, p: int) -> int:
        if n < p and m < p:
            return cal(n, m, p)
        else:
            return cal(n % p, m % p, p) * _lucas(n // p, m // p, p) % p

    n = int(input())
    for _ in range(n):
        a, b, p = map(int, input().split())
        print(_lucas(a, b, p))

if __name__ == "__main__":
    main()