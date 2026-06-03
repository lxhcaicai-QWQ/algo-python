
def main():
    N = 5050
    vis = [False] * N
    prime = []
    def _get_prime(n: int):
        for i in range(2, n + 1):
            if not vis[i]:
                prime.append(i)
            for x in prime:
                if i * x > n:
                    break
                vis[i * x] = True
                if i % x == 0:
                    break

    def get(n, p: int) -> int:
        res = 0
        while n != 0:
            res += n // p
            n //= p
        return res


    a,b = map(int, input().split())
    _get_prime(a)

    ans = 1
    for p in prime:
        count = get(a, p) - get(a - b, p) - get(b, p)
        ans = ans * (p ** count)

    print(ans)


if __name__ == "__main__":
    main()