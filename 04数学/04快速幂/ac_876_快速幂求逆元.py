

def main():
    def _kms(a,b,p: int) -> int:
        res = 1
        a %=p
        while b!=0:
            if b&1 == 1:
                res = res * a % p
            a = a * a % p
            b >>= 1
        return res

    def _gcd(a, b: int) -> int:
        if b == 0:
            return a
        return _gcd(b, a%b)

    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        if _gcd(a,b) == 1:
            print(_kms(a,b -2, b))
        else:
            print("impossible")

if __name__ == "__main__":
    main()