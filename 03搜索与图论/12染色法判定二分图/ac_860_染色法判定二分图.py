import sys

sys.setrecursionlimit(10**5)

def main():
    n,m = map(int, input().split())

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    color = [0] * (n + 1)

    def _dfs(x: int, c: int) -> bool:
        color[x] = c
        for y in g[x]:
            if color[y] == 0:
                 if not _dfs(y, 3 - c):
                     return False
            elif color[y] == color[x]:
                return False
        return True


    for i in range(1, n + 1):
        if color[i] == 0:
            if not _dfs(i, 1):
                print("No")
                return

    print("Yes")


if __name__ == "__main__":
    main()