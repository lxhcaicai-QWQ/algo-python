def main():
    n, m = map(int, input().split())

    fa = [i for i in range(n + 1)]

    """
        def _find(x: int) -> int:
            if x == fa[x]:
                return x
            fa[x] = _find(fa[x])
            return fa[x]
    """
    # （迭代，永不爆栈）
    def _find(x: int) -> int:
        root = x
        while root != fa[root]:
            root = fa[root]
        while x != root:
            nxt = fa[x]
            fa[x] = root
            x = nxt
        return root

    for _ in range(m):
        command = input().split()
        a = _find(int(command[1]))
        b = _find(int(command[2]))
        if command[0] == 'M':
            if a == b:
                continue
            fa[a] = b
        elif command[0] == 'Q':
            print("Yes" if a == b else "No")

if __name__ == "__main__":
    main()