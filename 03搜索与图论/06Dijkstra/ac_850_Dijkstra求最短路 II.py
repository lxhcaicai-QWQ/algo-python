import heapq


def main():
    n,m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b,c))


    INF = float('inf')
    dis = [INF] * (n + 1)
    def _dijkstra(st: int) -> None:
        dis[st] = 0
        heap = [(0, 1)]
        vis = [False] * (n + 1)
        while heap:
            d, x = heapq.heappop(heap)
            if vis[x]:
                continue
            vis[x] = True
            for y, z in graph[x]:
                if dis[y] > dis[x] + z:
                    dis[y] = dis[x] + z
                    heapq.heappush(heap, (dis[y], y))

    _dijkstra(1)
c


if __name__ == "__main__":
    main()