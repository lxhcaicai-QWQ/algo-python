
def main():
    n = int(input())

    def _gcd(x, y: int) -> int:
        if y == 0:
            return x
        return _gcd(y, x%y)

    for _ in range(n):
        a, b = map(int, input().split())
        print(_gcd(a,b))

if __name__ == "__main__":
    main()