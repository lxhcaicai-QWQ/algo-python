
def main():
    n = int(input())

    phi = [0] * (n + 1)
    primes = []
    def _get_prime(n: int):
        vis = [False] * (n + 1)
        phi[1] = 1
        for i in range(2,n + 1):
            if not vis[i]:
                phi[i] = i - 1
                primes.append(i)

            for x in primes:
                if i * x > n:
                    break
                vis[i * x] = True
                if i % x == 0:
                    phi[i * x] = phi[i] * x
                else:
                    phi[i * x] = phi[i] * (x - 1)

    _get_prime(n)
    print(sum(phi))

if __name__ == "__main__":
    main()