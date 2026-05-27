def main():
    n1, n2, m = map(int, input().split())
    g = [[] for _ in range(n1 + n2 +  2)]

    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b + n1)
        g[b + n1].append(a)

    vis = [0] * (n1 + n2 + 2)
    match = [0] * (n1 + n2 + 2)
    cnt = 0
    def _dfs(x: int) -> bool:
        for y in g[x]:
            if vis[y] != cnt:
                vis[y] = cnt
                if match[y] == 0 or _dfs(match[y]):
                    match[y] = x
                    return True
        return False

    ans = 0
    for i in range(1, n1 + 1):
        cnt += 1
        if match[i] == 0:
            if _dfs(i):
                ans +=1

    print(ans)

if __name__ == "__main__":
    main()