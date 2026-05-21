ans = 10 ** 10
def main():
    n = int(input())
    g = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a,b = map(int,input().split())
        g[a].append(b)
        g[b].append(a)

    def dfs(x, fa: int) -> int:
        global ans
        size, sums = 0, 0
        for y in g[x]:
            if y == fa:
                continue
            s = dfs(y, x)
            size = max(size, s)
            sums += s

        size = max(size, n - 1 - sums)
        ans = min(ans, size)
        return sums + 1
    dfs(1, 0)
    print(ans)
if __name__ == "__main__":
    main()