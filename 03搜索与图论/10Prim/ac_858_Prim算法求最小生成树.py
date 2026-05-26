INF = 10 ** 10
def main():
    n, m = map(int, input().split())
    g = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        x,y,z = map(int, input().split())
        g[x][y] = g[y][x] = min(g[x][y], z)

    def _prime():
        dis = [INF] * (n + 1)
        vis = [False] * (n + 1)
        res = 0
        for i in range(n):
            t = -1
            for j in range(1, n + 1):
                if not vis[j] and (t == -1 or dis[t] > dis[j]):
                    t = j

            if i > 0 and dis[t] == INF:
                return INF

            if i > 0:
                res += dis[t]
            vis[t] = True

            for j in range(1, n + 1):
                dis[j] = min(dis[j], g[t][j])

        return res

    res = _prime()

    if res == INF:
        print("impossible")
    else:
        print(res)
if __name__ == "__main__":
    main()