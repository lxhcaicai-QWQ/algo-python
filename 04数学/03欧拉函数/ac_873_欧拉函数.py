
def main():
    n = int(input())

    def _get_phi(x: int) -> int:
        ans = x
        i = 2
        while i * i <= x:
            if x % i == 0:
                ans = ans // i * (i - 1)
                while x % i == 0:
                    x //= i
            i += 1
        if x > 1:
            ans = ans // x * (x - 1)
        return ans

    for _ in range(n):
        x = int(input())
        print(_get_phi(x))

if __name__ == "__main__":
    main()