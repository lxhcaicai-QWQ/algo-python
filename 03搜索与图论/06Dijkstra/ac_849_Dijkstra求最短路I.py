
INF = 10 ** 10

def main():
    n,m = map(int, input().split())

    g = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a][b] = min(g[a][b],c)

    dis = [INF] * (n + 1)
    def _dijkstra(st: int) -> None:
        dis[st] = 0
        vis = [False] * (n + 1)
        for _ in range(n):
            t: int = -1
            for j in range(1,n + 1):
                if not vis[j] and (t == -1 or dis[t] > dis[j]):
                    t = j
            vis[t] = True
            for j in range(1, n + 1):
                dis[j] = min(dis[j], dis[t] + g[t][j])

    _dijkstra(1)
    print(-1 if dis[n] == INF else dis[n])


if __name__ == "__main__":
    main()