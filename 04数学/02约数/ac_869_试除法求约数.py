
def main():
    n = int(input())

    def _get_factor(x: int) -> list[int]:
        res = []
        i = 1
        while i * i <= x:
            if x % i == 0:
                res.append(i)
                if x // i != i:
                    res.append(x // i)
            i += 1

        res.sort()
        return res

    for _ in range(n):
        a = int(input())
        res = _get_factor(a)
        print(*res)
if __name__ == "__main__":
    main()