def main():
    n = int(input())

    grid = [['.'] * n for _ in range(n)]

    col = [False] * n
    sta1 = [False] * (2 * n)
    sta2 = [False] * (2 * n)

    def _dfs(d: int):
        if d == n:
            for i in range(n):
                print(''.join(grid[i]))
            print()
            return
        for i in range(n):
            if col[i] or sta1[d + i] or sta2[d - i + n]:
                continue
            col[i] = sta1[d + i] = sta2[d - i + n] = True
            grid[d][i] = 'Q'
            _dfs(d + 1)
            grid[d][i] = '.'
            col[i] = sta1[d + i] = sta2[d - i + n] = False

    _dfs(0)
if __name__ == "__main__":
    main()
