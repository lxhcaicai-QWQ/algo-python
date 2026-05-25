import copy
INF = 10**10

def main():
    n, m, k = map(int, input().split())
    edges = []
    for _ in range(m):
        x, y, z = map(int,input().split())
        edges.append((x, y, z))

    dis = [INF] * (n + 1)
    dis[1] = 0
    def _bellmanford(k: int):

        for _ in range(k):
            last = copy.deepcopy(dis)
            for j in range(m):
                x, y, z = edges[j]
                dis[y] = min(dis[y], last[x] + z)

    _bellmanford(k)
    if dis[n] > INF//2:
        print("impossible")
    else:
        print(dis[n])

if __name__ == "__main__":
    main()