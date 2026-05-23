import collections


def main():
    n,m = map(int, input().split())

    g = [[] for _ in range(n + 1)]
    deg = [0] * (n +  1)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        deg[b] += 1


    def _topo():
        deque = collections.deque()
        for i in range(1, n + 1):
            if deg[i] == 0:
                deque.append(i)

        res = []
        while len(deque) > 0:
            x = deque.popleft()
            res.append(x)
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 0:
                    deque.append(y)

        if len(res) != n:
            print(-1)
        else:
            print(*res)
    _topo()

if __name__ == "__main__":
    main()