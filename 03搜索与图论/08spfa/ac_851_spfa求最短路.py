import collections

INF = 10 ** 10

def main():
    n,m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a,b,c = map(int, input().split())
        graph[a].append((b,c))

    dis = [INF] * (n + 1)

    def _spfa(st: int):
        sta = [False] * (n + 1)
        deque = collections.deque()
        deque.append(st)
        dis[st] = 0
        while len(deque) > 0:
            x = deque.popleft()
            sta[x] = False
            for y,z in graph[x]:
                if dis[y] > dis[x] + z:
                    dis[y] = dis[x] + z
                    if not sta[y]:
                        sta[y] = True
                        deque.append(y)

    _spfa(1)
    if dis[n] == INF:
        print("impossible")
    else:
        print(dis[n])

if __name__ == "__main__":
    main()