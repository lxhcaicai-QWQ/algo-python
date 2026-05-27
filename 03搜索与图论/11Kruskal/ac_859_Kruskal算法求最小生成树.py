
def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a,b,c = map(int, input().split())
        edges.append((a,b,c))

    def _kruskal():
        fa = list(range(n + 1))
        def _find(x: int):
            if fa[x] == x:
                return x
            else:
                fa[x] = _find(fa[x])
                return fa[x]

        edges.sort(key=lambda x: x[2])
        ans = 0
        cnt = 0
        for a,b,c in edges:
            a = _find(a)
            b = _find(b)
            if a != b:
                ans += c
                cnt += 1
                fa[a] = b

            if cnt == n -1:
                break

        if cnt != n -1:
            print("impossible")
        else:
            print(ans)

    _kruskal()

if __name__ == "__main__":
    main()