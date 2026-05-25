import collections

INF = 10 ** 10
def main():
    n,m = map(int,input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))

    for i in range(1, n + 1):
        graph[0].append((i, 0))

    dis = [INF] * (n + 1)
    def _spfa(st: int) -> str:
        dis[st] = 0
        cnt = [0] * (n + 1)
        sta = [False] * (n + 1)
        deque = collections.deque()
        deque.append(st)
        while len(deque) > 0:
            x = deque.popleft()
            sta[x] = False

            for y,z in graph[x]:
                if dis[y] > dis[x] + z:
                    dis[y] = dis[x] + z
                    cnt[y] = cnt[x] + 1
                    if cnt[y] > n:
                        return "Yes"
                    if not sta[y]:
                        deque.append(y)
        return "No"


    print(_spfa(0))
if __name__ == "__main__":
    main()