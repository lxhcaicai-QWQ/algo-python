
def main():
    n = int(input())

    def _prime(m: int) -> list[int]:
        primes = []
        vis = [False] * (n + 1)
        for i in range(2, n + 1):
            if not vis[i]:
                primes.append(i)
            for p  in primes:
                if i * p > n:
                    break
                vis[i * p] = True
                if i % p == 0:
                    break
        return primes

    lst = _prime(n)

    print(len(lst))

if __name__ == "__main__":
    main()