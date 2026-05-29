def main():
    n = int(input())
    count_map = {}
    MOD = 10 ** 9 + 7

    def _insert(x, num: int):
        count_map[x] = count_map.get(x, 0) + num

    def get_div(x: int):
        i = 2
        while i * i <= x:
            cnt = 0
            if x % i == 0:
                while x % i == 0:
                    x //= i
                    cnt += 1
                _insert(i, cnt)
            i += 1
        if x > 1:
            _insert(x, 1)

    for _ in range(n):
        a = int(input())
        get_div(a)

    ans = 1
    for item in count_map.values():
        ans = ans * (item + 1) % MOD

    print(ans)


if __name__ == "__main__":
    main()