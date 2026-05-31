
def main():

    def _ksm(a,b,p: int) -> int:
        res = 1
        a %= p
        while b!=0:
            if b&1 == 1:
                res = res * a % p
            a = a * a % p
        return res

    n = int(input())
    for _ in range(n):
        a, b, p = map(int, input())
        print(_ksm(a, b, p))


if __name__ == "__main__":
    main()