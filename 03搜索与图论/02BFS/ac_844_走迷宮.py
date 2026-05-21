import collections

def bfs(n, m: int, g: list[list[int]]):
    deque = collections.deque()
    deque.append((0, 0, 0))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    vis = [[False] * m for _ in range(n)]
    while len(deque) > 0:
        x, y, dis = deque.popleft()
        if vis[x][y]:
            continue
        vis[x][y] = True
        if x == n - 1 and y == m - 1:
            return dis
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != 1:
                deque.append((nx, ny, dis + 1))

    return -1


def main():
    n, m = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    print(bfs(n, m, g))

if __name__ == "__main__":
    main()