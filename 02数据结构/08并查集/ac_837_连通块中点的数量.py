
def main():
    n, m = map(int, input().split())

    fa = [i for i in range(n + 1)]
    cnt = [1] * (n + 1)
    cnt[0] = 0

    def _find(x: int) -> int:
        root = x
        while root != fa[root]:
            root = fa[root]
        while x != root:
            nxt = fa[x]
            fa[x] = root
            x = nxt
        return root

    def _merge(a, b: int):
        fa[a] = b
        cnt[b] += cnt[a]

    for _ in  range(m):
        command = input().split()
        if command[0] == 'C':
            a = _find(int(command[1]))
            b = _find(int(command[2]))
            if a != b:
                _merge(a, b)

        elif command[0] == 'Q1':
            a = _find(int(command[1]))
            b = _find(int(command[2]))
            print("Yes" if a == b else "No")

        elif command[0] == "Q2":
            a = _find(int(command[1]))
            print(cnt[a])

if __name__ == "__main__":
    main()