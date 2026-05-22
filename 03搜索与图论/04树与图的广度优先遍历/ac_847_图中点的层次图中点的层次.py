import collections


def bfs(n:int, g: list[list[int]]) -> int:
    dis = [-1] * (n + 1)
    dis[1] = 0
    deque = collections.deque()
    deque.append(1)
    while len(deque) > 0:
        x = deque.popleft()
        for y in g[x]:
            if dis[y] == -1:
                dis[y] = dis[x] + 1
                deque.append(y)

    return dis[n]

def main():
    n, m = map(int, input().split())

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)

    print(bfs(n, g))


if __name__ == "__main__":
    main()