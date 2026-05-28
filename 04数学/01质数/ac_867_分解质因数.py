
def main():
    n = int(input())

    def _solve(x: int):
        i = 2
        while i * i <= x:
            if x%i == 0:
                cnt = 0
                while x % i ==0:
                    cnt += 1
                    x /= i
                print(i, cnt)
            i += 1
        if x > 1:
            print(int(x), 1)
        print()

    for _ in range(n):
        a = int(input())
        _solve(a)

if __name__ == "__main__":
    main()